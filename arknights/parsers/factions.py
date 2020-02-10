from arknights.parsers.parser import Parser


class FactionParser(Parser):
    def parse(self, response):
        yield {
            "_dir": "factions",
            "name": response.css("h1::text").get(default="").strip(),
        }
