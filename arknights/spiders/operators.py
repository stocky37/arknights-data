# -*- coding: utf-8 -*-
from scrapy import Spider
from slugify import slugify


class OperatorsSpider(Spider):
    name = "operators"
    allowed_domains = ["en.rhinelab.org"]
    start_urls = ["http://en.rhinelab.org/List_of_Operators_by_Image"]
    slug = "name"

    def parse(self, response):
        for a in response.css(".charbadge-name > a"):
            yield response.follow(a, self.parse_operator)

    @staticmethod
    def parse_operator(response):
        def extract(query, base=response):
            return base.css(query).get(default="").strip()

        name = extract(".character-name::text")
        if not name:
            name = extract("h1::text")
        icons = response.css(".character-icon")

        yield {
            "name": name,
            "stars": len(response.css(".character-stars span")),
            "class": slugify(extract("a::attr(title)", icons[0])),
            "faction": slugify(extract("a::attr(title)", icons[1])),
        }
