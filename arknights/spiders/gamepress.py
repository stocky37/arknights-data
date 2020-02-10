from scrapy import Spider

from arknights.parsers.gamepress.operators import OperatorParser


class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ["gamepress.gg"]
    start_urls = ["https://gamepress.gg/arknights/database/operators"]
    slug = "name"

    def __init__(self, *args, **kwargs):
        super(WikiSpider, self).__init__(*args, **kwargs)
        self.operatorParser = OperatorParser(self)

    def parse(self, response):
        for a in response.css(".charbadge-name > a"):
            yield response.follow(a, self.operatorParser.parse)
