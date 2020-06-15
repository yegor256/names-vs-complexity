import os
import sys
import unittest
import javalang
from glob import glob

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

fileDir = os.path.dirname(os.path.realpath('__file__'))
testargs = ["", os.path.join(fileDir, 'java/cc/SwitchCaseStatement.java')]
with patch.object(sys, 'argv', testargs):
    from calc import branches

def cc(tree):
    var = next(tree.filter(javalang.tree.VariableDeclarator))[1]
    if (var.name != 'cc'):
        raise ValueError('file not tested')
    return int(var.initializer.value)

for java in glob('java/cc/*.java'):
    with open(java, encoding='utf-8') as f:
        try:
            ast = javalang.parse.parse(f.read())
            received = 1
            expected = cc(ast)

            for path, node in ast:
                received += branches(node)

            if (received != expected):
                raise Exception('\nTest failed. Expected ' + str(expected) + ', received ' + str(received))

            print('.', end='', flush=True),
        except Exception as e:
            sys.exit(str(e) + ': ' + java)

print(' OK')

