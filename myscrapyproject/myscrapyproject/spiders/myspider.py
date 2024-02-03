import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]

    def parse(self, response):
        # # Extract information only from the first section of the page
        # section_selector = response.css('div#mw-content-text > div.mw-parser-output > *:first-child')
        # section_content = section_selector.extract()
        #
        # # Process or yield the extracted data as needed
        # # step where you take the information you have extracted from a webpage and decide what to do with it
        # yield {
        #     'section_content': section_content,
        # }

        # Extract title and content
        title = response.css('title::text').get()
        # content = response.css('div#mw-content-text > div.mw-parser-output > *:first-child').get()
        content = response.css('div#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(6)').get()

        # Display the extracted data
        self.log(f'Title: {title}')
        self.log(f'Content: {content}')

        # Optionally, yield the extracted data for further processing
        yield {
            'title': title,
            'content': content,
        }



