import sys
import javalang
import itertools
from glob import glob
from Metric import Metric

def expected(tree):
    var = next(tree.filter(javalang.tree.VariableDeclarator))[1]
    if (var.name != 'expected'):
        raise ValueError('file not tested')
    return int(var.initializer.value)

for java in glob('java/clones/*.java'):
    with open(java, encoding='utf-8') as f:
        try:
            tree = javalang.parse.parse(f.read())
            metric = Metric(tree)
            if (metric.cc() != expected(tree)):
                raise Exception('test failed')
            print('.', end='', flush=True),
        except Exception as e:
            sys.exit(str(e) + ': ' + java)

print('OK')

