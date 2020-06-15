from javalang import tree

class Branch:
    def __init__(self, node):
        self.node = node

    def count(self):
        if (isinstance(self.node, tree.BinaryOperation)):
            if(self.node.operator == '&&' or self.node.operator == '||'):
                return 1

        if(isinstance(self.node, (
            tree.ForStatement,
            tree.IfStatement,
            tree.WhileStatement,
            tree.DoStatement,
            tree.TernaryExpression
        ))):
            return 1

        if(isinstance(self.node, tree.SwitchStatementCase)):
            return len(self.node.case)

        return 0

