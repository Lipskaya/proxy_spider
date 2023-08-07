# proxy_spider
Test task 
## How to run
* set environment variable `API_KEY` for [scraperapi.com](https://scraperapi.com)
* run `pip install scrapy`
* run `scrapy startproject bestsellers`
* copy `proxy_spider.py` from this repo to `/spiders` folder of created **besselers** project
* run from `/besselers` folder next command ```scrapy crawl my_spider```
* find result in generated `extracted_data.json` file
