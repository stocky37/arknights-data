# -*- coding: utf-8 -*-
from scrapy import Spider

from arknights.parsers.wiki.classes import ClassParser
from arknights.parsers.wiki.factions import FactionParser
from arknights.parsers.wiki.operators import OperatorParser


class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ["en.rhinelab.org"]
    start_urls = ["http://en.rhinelab.org/List_of_Operators_by_Image"]
    slug = "name"

    def __init__(self, *args, **kwargs):
        super(WikiSpider, self).__init__(*args, **kwargs)
        self.operatorParser = OperatorParser(self)
        self.factionParser = FactionParser(self)
        self.classParser = ClassParser(self)

    def parse(self, response):
        for a in response.css(".charbadge-name > a"):
            yield response.follow(a, self.operatorParser.parse)
