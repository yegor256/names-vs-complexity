import javalang
from unittest import TestCase
from Branch import Branch

class Branch_Test(TestCase):
    def test_for_statement_exists(self):
        code = """
            for (int i = 0; i < amounts.length; i++) {
                result += amounts[i];
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).exists(), True)

    def test_branch_not_exists(self):
        code = "nextKey = new BlockKey(serialNo, System.currentTimeMillis() + 3.0);"
        node = self.expression(code)
        self.assertEqual(Branch(node).exists(), False)

    def test_if_statement_exists(self):
        code = """
            if (itr == '\r') {
                int status = 1;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).exists(), True)

    def test_while_statement_exists(self):
        code = """
            while (i < 5) {
                System.out.println(i);
                i++;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).exists(), True)

    def test_do_statement_exists(self):
        code = """
            do
                a-- ;
            while ( a );
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).exists(), True)

    def test_switch_statement_exists(self):
        code = """
            switch ( a )
            {
                case 1:
                return ;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node.cases[0]).exists(), True)

    def test_logic_and_operator_exists(self):
        code = 'if ( a && b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).exists(), True)

    def test_logic_or_operator_exists(self):
        code = 'if ( a || b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).exists(), True)

    def test_logic_operator_not_exists(self):
        code = 'if ( a > b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).exists(), False)

    def test_ternary_operator(self):
        code = 'value == "uppercase" ? "JOHN" : "john";'
        node = self.expression(code);
        self.assertEqual(Branch(node).exists(), True)

    def expression(self, code):
        return self.parser(code).parse_expression()

    def statement(self, code):
        return self.parser(code).parse_statement()

    def parser(self, code):
        return javalang.parser.Parser(
            javalang.tokenizer.tokenize(code)
        )

