import json
import os


class JsonMergePipeline(object):
    @staticmethod
    def process_item(item, spider):
        filename = spider.settings.get("FILENAME_TEMPLATE").format(
            item["_dir"], item["slug"]
        )

        existing = None
        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as f:
                existing = json.load(f)

        return item if not existing else {**existing, **item}
