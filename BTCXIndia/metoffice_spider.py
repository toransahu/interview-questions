"""Crawing using scrapy."""
import scrapy


class WeatherSpider(scrapy.Spider):
    """Crawl www.metoffice.gov.uk."""

    name = 'weatherspider'
    start_urls = ['https://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder']

    def parse(self, response):
        """Parse Title and Pages."""
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
