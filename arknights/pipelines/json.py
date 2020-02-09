import json


class JsonPipeline(object):
    @staticmethod
    def process_item(item, _):
        filename = "data/operators/" + item["slug"] + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(item, f, indent=2, sort_keys=True)
        return item
