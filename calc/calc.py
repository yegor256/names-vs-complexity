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
import javalang

def ncss(tree):
    metric = 0
    print(tree.types[0].body[0])
    return
    print('node_type list\n')
    for path, node in tree:
        node_type = str(type(node))
        if 'IfStatement' in node_type:
            metric += 1
        elif 'VariableDeclarator' in node_type:
            print(str(node.initializer.value));
    return metric

java = sys.argv[1]
with open(java, encoding='utf-8') as f:
    try:
        raw = javalang.parse.parse(f.read())
        # tree = raw.filter(javalang.tree.ClassDeclaration)
        ncss(raw)
        # print(str(ncss(raw))
    except Exception as e:
        sys.exit(str(e) + ': ' + java)
