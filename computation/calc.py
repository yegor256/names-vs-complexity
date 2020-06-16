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
import re
from javalang import tree, parse

"""Determines the number of branches for a node
according to the Extended Cyclomatic Complexity metric.
Binary operations (&&, ||) and each case statement are taken into account.

:param node: class provided by the parser and targeted to Java 8 spec
:returns: number
"""
def branches(node):
    count = 0
    if (isinstance(node, tree.BinaryOperation)):
        if(node.operator == '&&' or node.operator == '||'):
            count = 1
    elif(isinstance(node, (
        tree.ForStatement,
        tree.IfStatement,
        tree.WhileStatement,
        tree.DoStatement,
        tree.TernaryExpression
    ))):
        count = 1
    elif(isinstance(node, tree.SwitchStatementCase)):
        count = len(node.case)
    elif(isinstance(node, tree.TryStatement)):
        count = len(node.catches)
    return count

"""Check the name for compound inside the methods (i.e. for local variables)

:param node: class provided by the parser and targeted to Java 8 spec
:returns: boolean
"""
def compound(node):
    flag = False
    if (isinstance(node, tree.LocalVariableDeclaration)):
        name = node.declarators[0].name
        flag = len(re.findall(r'(?:[a-z][A-Z]+)|(?:[_])', name)) != 0
    return flag


java = sys.argv[1]
with open(java, encoding='utf-8') as f:
    try:
        cc = 1
        names = 0
        ast = parse.parse(f.read())
        for path, node in ast:
            cc += branches(node)
            names += int(compound(node))
        print(str(cc) + ',' +  str(names))
    except Exception as e:
        sys.exit(str(e) + ': ' + java)
