from javalang import tree

class Branch:
    def __init__(self, node):
        self.node = node

    def exists(self):
        if (isinstance(self.node, tree.BinaryOperation)):
            return self.node.operator == '&&' or self.node.operator == '||'

        return isinstance(self.node, (
            tree.ForStatement,
            tree.IfStatement,
            tree.WhileStatement,
            tree.DoStatement,
            tree.SwitchStatementCase,
            tree.TernaryExpression
        ))

