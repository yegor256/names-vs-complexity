from javalang.tree import ForStatement

class Branch:
    def __init__(self, node):
        self.node = node

    def exists(self):
        return self.forStatement()

    def forStatement(self):
        return isinstance(self.node, ForStatement)
