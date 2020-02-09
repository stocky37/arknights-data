import json


class JsonPipeline(object):
    @staticmethod
    def process_item(item, spider):
        filename = spider.settings.get("FILENAME_TEMPLATE").format(
            spider.name, item["slug"]
        )
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(item, f, indent=2, sort_keys=True)
            f.write("\n")
        return item
