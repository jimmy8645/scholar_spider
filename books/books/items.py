# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GoogleScholarItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    publication_year = scrapy.Field()
    citation_count = scrapy.Field()
    url = scrapy.Field()
    snippet = scrapy.Field()
    journal = scrapy.Field()
    legitimacy_score = scrapy.Field()
