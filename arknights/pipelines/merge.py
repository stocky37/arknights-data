import json


class JsonMergePipeline(object):
    @staticmethod
    def process_item(item, spider):
        filename = spider.settings.get("FILENAME_TEMPLATE").format(
            spider.name, item["slug"]
        )
        with open(filename, encoding="utf-8") as f:
            existing = json.load(f)
        return {**existing, **item}
