# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from datetime import datetime


class BooksPipeline:
    def process_item(self, item, spider):
        return item

class GoogleScholarPipeline:
    def process_item(self, item, spider):
        # compute legitimacy score: citations normalized by publication age
        citations = int(item.get('citation_count', 0) or 0)
        year = item.get('publication_year')
        try:
            age = datetime.now().year - int(year) + 1
        except Exception:
            age = 1
        item['legitimacy_score'] = citations / age if age > 0 else 0
        return item
