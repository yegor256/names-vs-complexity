import javalang
from unittest import TestCase
from Branch import Branch

class Branch_Test(TestCase):
    # def ttest_if_statement(self):
    #     code = "class NewOne {}"
    #     node = parser.Parser(tokenizer.tokenize(code));
    #     branch = Branch(node)
    #     self.assertEqual(branch.exists(), False)

    def test_for_statement_exists(self):
        code = """
            for (int i = 0; i < amounts.length; i++) {
                result += amounts[i];
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).forStatement(), True)

    def test_for_statement_not_exists(self):
        code = """
            if (itr == '\r') {
                int status = 1;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).forStatement(), False)

    def statement(self, code):
        return javalang.parser.Parser(
            javalang.tokenizer.tokenize(code)
        ).parse_statement()

