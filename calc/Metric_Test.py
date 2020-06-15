import javalang
from unittest import TestCase
from unittest.mock import create_autospec, patch, Mock
from Metric import Metric

class Metric_Test(TestCase):
    def test_metric_when_branches_count(self):
        with patch('Metric.Branch') as MockClassBranch:
            MockBranch = MockClassBranch.return_value
            MockBranch.count.return_value = True
            code = 'nextKey = new BlockKey(serialNo, System.currentTimeMillis() + 3);'
            self.assertEqual(Metric(self.tree(code)).cc(), 10)

    def test_metric_when_branches_not_count(self):
        with patch('Metric.Branch') as MockClassBranch:
            MockBranch = MockClassBranch.return_value
            MockBranch.count.return_value = False
            code = 'nextKey = new BlockKey(serialNo, System.currentTimeMillis() + 3);'
            self.assertEqual(Metric(self.tree(code)).cc(), 1)

    def tree(self, code):
        return javalang.parser.Parser(
            javalang.tokenizer.tokenize(code)
        ).parse_statement()
