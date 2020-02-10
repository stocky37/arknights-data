from abc import ABC


class Parser(ABC):
    def __init__(self, spider=None):
        self.spider = spider

    def parse(self, response):
        pass
