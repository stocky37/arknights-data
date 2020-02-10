# -*- coding: utf-8 -*-
from scrapy import Spider
from slugify import slugify


class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ["en.rhinelab.org"]
    start_urls = ["http://en.rhinelab.org/List_of_Operators_by_Image"]
    slug = "name"

    def parse(self, response):
        for a in response.css(".charbadge-name > a"):
            yield response.follow(a, self.parse_operator)

    def parse_operator(self, response):
        name = response.css(".character-name::text").get(default="").strip()
        if not name:
            name = response.css("h1::text").get(default="").strip()

        try:
            [clazz_a, faction_a] = response.css(".character-icon .text > a")
            clazz = slugify(clazz_a.attrib.get("text", ""))
            faction = slugify(faction_a.attrib.get("text", ""))
        except ValueError:
            clazz_a = None
            faction_a = None
            clazz = None
            faction = None

        yield {
            "_dir": "operators",
            "name": name,
            "stars": len(response.css(".character-stars span") or 0),
            "class": clazz,
            "faction": faction,
        }

        if clazz_a:
            yield response.follow(clazz_a, self.parse_class)
        if faction_a:
            yield response.follow(faction_a, self.parse_faction)

    def parse_class(self, response):
        pass

    def parse_faction(self, response):
        pass
