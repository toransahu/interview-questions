"""Crawing using scrapy."""
import scrapy


class BlogSpider(scrapy.Spider):
    """Crawl Blog.Scrapinghub.Com."""

    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        """Parse Title and Pages."""
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
