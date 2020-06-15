import javalang
from unittest import TestCase
from Branch import Branch

class Branch_Test(TestCase):
    def test_for_statement_count(self):
        code = """
            for (int i = 0; i < amounts.length; i++) {
                result += amounts[i];
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).count(), 1)

    def test_branch_not_count(self):
        code = "nextKey = new BlockKey(serialNo, System.currentTimeMillis() + 3.0);"
        node = self.expression(code)
        self.assertEqual(Branch(node).count(), 0)

    def test_if_statement_count(self):
        code = """
            if (itr == '\r') {
                int status = 1;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).count(), 1)

    def test_while_statement_count(self):
        code = """
            while (i < 5) {
                System.out.println(i);
                i++;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).count(), 1)

    def test_do_statement_count(self):
        code = """
            do
                a-- ;
            while ( a );
        """
        node = self.statement(code)
        self.assertEqual(Branch(node).count(), 1)

    def test_switch_statement_count(self):
        code = """
            switch ( a )
            {
                case 1:
                return ;
            }
        """
        node = self.statement(code)
        self.assertEqual(Branch(node.cases[0]).count(), 1)

    def test_logic_and_operator_count(self):
        code = 'if ( a && b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).count(), 1)

    def test_logic_or_operator_count(self):
        code = 'if ( a || b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).count(), 1)

    def test_logic_operator_not_count(self):
        code = 'if ( a > b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(Branch(ifNode.children[1]).count(), 0)

    def test_ternary_operator(self):
        code = 'value == "uppercase" ? "JOHN" : "john";'
        node = self.expression(code);
        self.assertEqual(Branch(node).count(), 1)

    def expression(self, code):
        return self.parser(code).parse_expression()

    def statement(self, code):
        return self.parser(code).parse_statement()

    def parser(self, code):
        return javalang.parser.Parser(
            javalang.tokenizer.tokenize(code)
        )

