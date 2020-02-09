from slugify import slugify


class SlugifyPipeline(object):
    @staticmethod
    def process_item(item, spider):
        item["slug"] = slugify(item[spider.slug])
        return item
