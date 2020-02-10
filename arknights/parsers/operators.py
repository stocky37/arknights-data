from slugify import slugify

from arknights.parsers.parser import Parser


class OperatorParser(Parser):
    def parse(self, response):
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
            yield response.follow(clazz_a, self.spider.classParser.parse)
        if faction_a:
            yield response.follow(faction_a, self.spider.factionParser.parse)
