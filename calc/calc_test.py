import sys
import javalang
import itertools
from glob import glob
from Metric import Metric

def cc(tree):
    var = next(tree.filter(javalang.tree.VariableDeclarator))[1]
    if (var.name != 'cc'):
        raise ValueError('file not tested')
    return int(var.initializer.value)

for java in glob('java/*.java'):
    with open(java, encoding='utf-8') as f:
        try:
            tree = javalang.parse.parse(f.read())
            received = Metric(tree).cc()
            expected = cc(tree)
            if (received != expected):
                raise Exception('test failed. Expected ' + str(expected) + ', received ' + str(received))
            print('.', end='', flush=True),
        except Exception as e:
            sys.exit(str(e) + ': ' + java)

print('OK')

