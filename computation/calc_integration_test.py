import os
import sys
import unittest
import javalang
from glob import glob
import re

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

fileDir = os.path.dirname(os.path.realpath('__file__'))
testargs = ["", os.path.join(fileDir, 'java/cc/SwitchCaseStatement.java')]
with patch.object(sys, 'argv', testargs):
    from calc import branches, compound

def cc(tree):
    var = next(tree.filter(javalang.tree.VariableDeclarator))[1]
    if (var.name != 'cc'):
        raise ValueError('file not tested')
    return int(var.initializer.value)

def names(ast):
    comment = next(ast.filter(javalang.tree.Documented))[1]
    return int(re.search(r'[\d]+', comment.documentation).group(0))

for java in glob('java/names/*.java'):
    with open(java, encoding='utf-8') as f:
        try:
            ast = javalang.parse.parse(f.read())
            receivedNames = 0
            expectedNames = names(ast)

            for path, node in ast:
                receivedNames += compound(node)

            if (receivedNames != expectedNames):
                raise Exception('\nTest failed. Expected ' + str(expectedNames) + ', receivedNames ' + str(receivedNames))
        except Exception as e:
            sys.exit(str(e) + ': ' + java)

for java in glob('java/cc/*.java'):
    with open(java, encoding='utf-8') as f:
        try:
            ast = javalang.parse.parse(f.read())
            receivedCC = 1
            expectedCC = cc(ast)

            for path, node in ast:
                receivedCC += branches(node)

            if (receivedCC != expectedCC):
                raise Exception('\nTest failed. Expected ' + str(expectedCC) + ', receivedCC ' + str(receivedCC))

            print('.', end='', flush=True),
        except Exception as e:
            sys.exit(str(e) + ': ' + java)

print(' OK')

