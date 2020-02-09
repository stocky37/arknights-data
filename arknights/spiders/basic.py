# -*- coding: utf-8 -*-
from slugify import slugify
from scrapy import Spider


class BasicSpider(Spider):
    name = "operators"
    allowed_domains = ["en.rhinelab.org"]
    start_urls = ["http://en.rhinelab.org/List_of_Operators_by_Image"]

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
        yield {
            "slug": slugify(name),
            "name": name,
            "stars": len(response.css(".character-stars span")),
        }
