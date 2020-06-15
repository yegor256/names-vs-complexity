from Branch import Branch
from javalang.tree import ForStatement

class Metric:
    num = 1

    def __init__(self, tree):
        self.tree = tree

    def cc(self):
        for path, node in self.tree:
            if (Branch(node).exists()):
                self.num += 1
        return self.num;
