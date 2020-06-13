from pkg_resources import resource_string
from javalang import parse

class Piu:
    def __init__(self, file):
        self.file = file

    def tree(self):
        source = resource_string(__name__, self.file)
        return parse.parse(source)
