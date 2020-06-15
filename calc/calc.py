# The MIT License (MIT)
#
# Copyright (c) 2020 Yegor Bugayenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from javalang import tree, parse

def branches(node):
    if (isinstance(node, tree.BinaryOperation)):
        if(node.operator == '&&' or node.operator == '||'):
            return 1

    if(isinstance(node, (
        tree.ForStatement,
        tree.IfStatement,
        tree.WhileStatement,
        tree.DoStatement,
        tree.TernaryExpression
    ))):
        return 1

    if(isinstance(node, tree.SwitchStatementCase)):
        return len(node.case)

    return 0


java = sys.argv[1]
with open(java, encoding='utf-8') as f:
    try:
        cc = 1
        ast = parse.parse(f.read())
        for path, node in ast:
            cc += branches(node)
    except Exception as e:
        sys.exit(str(e) + ': ' + java)
