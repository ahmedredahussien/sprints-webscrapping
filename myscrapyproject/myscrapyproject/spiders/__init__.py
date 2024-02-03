# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


# python -m venv venv
# .\venv\Scripts\activate
# pip install scrapy
# scrapy startproject myscrapyproject
# cd myscrapyproject
# scrapy genspider myspider https://en.wikipedia.org/wiki/Python_(programming_language)
# - start_urls
# scrapy crawl myspider
# scrapy crawl myspider -o output.json
# scrapy crawl myspider -o output.csv
# scrapy crawl myspider -o output.xml


# scrapy shell https://en.wikipedia.org/wiki/Python_(programming_language)
# response.css('title::text').get()
# response.css('div#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(6)').get()
# response.css('div#mw-content-text > div.mw-content-ltr.mw-parser-output > p).getall()
# response.css('div#mw-content-text > div.mw-content-ltr.mw-parser-output > p').getall()[4]
# response.css('div#mw-content-text > div.mw-content-ltr.mw-parser-output > p').getall()[4].strip().replace('\n', '')
