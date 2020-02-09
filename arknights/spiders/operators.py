# -*- coding: utf-8 -*-
from scrapy import Spider
from slugify import slugify


class OperatorsSpider(Spider):
    name = "operators"
    allowed_domains = ["en.rhinelab.org"]
    start_urls = ["http://en.rhinelab.org/List_of_Operators_by_Image"]
    slug = "name"

    def parse(self, response):
        for a in response.css(".charbadge-image > a"):
            yield response.follow(a, self.parse_operator)

    @staticmethod
    def parse_operator(response):
        def extract(query):
            return response.css(query).get(default="").strip()

        name = extract(".character-name::text")
        if not name:
            name = extract("h1::text")
        icons = response.css(".character-icon")

        yield {
            "name": name,
            "stars": len(response.css(".character-stars span")),
            "class": slugify(icons[0].css("a::attr(title)").get()),
            "faction": slugify(icons[1].css("a::attr(title)").get()),
        }
