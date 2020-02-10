from arknights.parsers.parser import Parser


class ClassParser(Parser):
    def parse(self, response):
        yield {
            "_dir": "classes",
            "name": response.css("h1::text").get(default="").strip(),
        }
