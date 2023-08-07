import scrapy
import json
import base64
import os

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def start_requests(self):
        urls = [
            'http://free-proxy.cz/en/'            
        ]

        meta = {
            "proxy": "http://scraperapi:" + os.environ.get("API_KEY") + "@proxy-server.scraperapi.com:8001"
            }

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)


    def parse(self, response):
        table_data = response.css('#proxy_list')

        extracted_data = []
        for row in table_data.css('tr')[1:]:
            if (len(row.css('td:nth-child(1) script::text').get().split('"'))==3):
                codedIp=row.css('td:nth-child(1) script::text').get().split('"')[1]
                data = {
                    'ipAdress': base64.b64decode(codedIp).decode('utf-8'),
                    'port': row.css('td:nth-child(2) span::text').get(),
                }
                extracted_data.append(data)

        filename = 'extracted_data.json'
        with open(filename, 'w') as json_file:
            json.dump(extracted_data, json_file)

        self.log(f'Saved data to {filename}')

