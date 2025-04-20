import re
import scrapy
from books.items import GoogleScholarItem

class GoogleScholarSpider(scrapy.Spider):
    name = 'google_scholar'
    allowed_domains = ['scholar.google.com']

    def __init__(self, query=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not query:
            raise ValueError("Query must be provided using -a query=<search term>")
        self.query = query
        self.start_urls = [f"https://scholar.google.com/scholar?q={query}"]

    def parse(self, response):
        for result in response.css('div.gs_ri'):
            item = GoogleScholarItem()
            item['title'] = result.css('h3.gs_rt a::text').get()
            item['url'] = result.css('h3.gs_rt a::attr(href)').get()
            authors_info = result.css('div.gs_a::text').get()
            parts = authors_info.split(' - ') if authors_info else []
            item['authors'] = parts[0] if parts else None
            if len(parts) > 1:
                journal_and_year = parts[1]
                year_match = re.search(r"\b(20\d{2}|19\d{2})\b", journal_and_year)
                item['publication_year'] = year_match.group(0) if year_match else None
                item['journal'] = journal_and_year.split(',')[0]
            else:
                item['publication_year'] = None
                item['journal'] = None
            citations_text = result.css('div.gs_fl a::text').re_first(r'Cited by \d+')
            item['citation_count'] = citations_text.replace('Cited by ', '') if citations_text else 0
            item['snippet'] = result.css('div.gs_rs::text').get()
            yield item

        next_page = response.css('div#gs_n td a.gs_nma::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)