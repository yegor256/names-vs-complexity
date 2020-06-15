from Branch import Branch
import javalang

class Metric:
    num = 1

    def __init__(self, tree):
        self.tree = tree

    def cc(self):
        for path, node in self.tree:
            self.num += Branch(node).count()
        return self.num;
