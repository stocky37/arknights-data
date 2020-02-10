import json


class JsonPipeline(object):
    def process_item(self, item, spider):
        filename = spider.settings.get("FILENAME_TEMPLATE").format(
            item["_dir"], item["slug"]
        )
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.filter(item), f, indent=2, sort_keys=True)
            f.write("\n")
        return item

    def filter(self, item):
        self.filter_meta_keys(item)
        return item

    @staticmethod
    def filter_meta_keys(item):
        for key in list(dict(item).keys()):
            if key.startswith("_"):
                del item[key]
        return item
