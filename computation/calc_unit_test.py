import os
import sys
import unittest
import javalang

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

fileDir = os.path.dirname(os.path.realpath(__file__))
testargs = ["", os.path.join(fileDir, 'java/cc/SwitchCaseStatement.java')]
with patch.object(sys, 'argv', testargs):
    from calc import branches, compound

class TestCalc(unittest.TestCase):
    def test_for_statement_count(self):
        code = """
            for (int i = 0; i < amounts.length; i++) {
                result += amounts[i];
            }
        """
        node = self.statement(code)
        self.assertEqual(branches(node), 1)

    def test_branch_not_count(self):
        code = "nextKey = new BlockKey(serialNo, System.currentTimeMillis() + 3.0);"
        node = self.expression(code)
        self.assertEqual(branches(node), 0)

    def test_if_statement_count(self):
        code = """
            if (itr == '\r') {
                int status = 1;
            }
        """
        node = self.statement(code)
        self.assertEqual(branches(node), 1)

    def test_while_statement_count(self):
        code = """
            while (i < 5) {
                System.out.println(i);
                i++;
            }
        """
        node = self.statement(code)
        self.assertEqual(branches(node), 1)

    def test_do_statement_count(self):
        code = """
            do
                a-- ;
            while ( a );
        """
        node = self.statement(code)
        self.assertEqual(branches(node), 1)

    def test_switch_statement_count(self):
        code = """
            switch ( a )
            {
                case 1:
                return ;
            }
        """
        node = self.statement(code)
        self.assertEqual(branches(node.cases[0]), 1)

    def test_logic_and_operator_count(self):
        code = 'if ( a && b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(branches(ifNode.children[1]), 1)

    def test_logic_or_operator_count(self):
        code = 'if ( a || b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(branches(ifNode.children[1]), 1)

    def test_logic_operator_not_count(self):
        code = 'if ( a > b ) {}'
        ifNode = self.statement(code)
        self.assertEqual(branches(ifNode.children[1]), 0)

    def test_ternary_operator(self):
        code = 'value == "uppercase" ? "JOHN" : "john";'
        node = self.expression(code);
        self.assertEqual(branches(node), 1)

    def test_catch_statements(self):
        code = """
            try {
                Throwable t = new Exception();
                throw t;
            } catch (RuntimeException e) {
                System.err.println("catch RuntimeException");
            } catch (Exception e) {
                System.err.println("catch Exception");
            } catch (Throwable e) {
                System.err.println("catch Throwable");
            }
            System.err.println("next statement");
        """
        node = self.statement(code)
        self.assertEqual(branches(node), 3)

    def test_compound_with_camel_and_snake_cases(self):
        for s in ['camelCase', 'CamelCase', 'camelCASE', 'snake_case', 'snake_CASE', 'SNAKE_CASE', 'SNAKE_case']:
            code = "int %s = 0;" % (s)
            node = self.parser(code).parse_method_or_field_declaraction()
            self.assertEqual(compound(node.declarators[0]), 1)

    def test_compound_without_camel_and_snake_cases(self):
        for s in ['camelcase, CAMELCASE, Camelcase']:
            code = "int %s = 0;" % (s)
            node = self.parser(code).parse_method_or_field_declaraction()
            self.assertEqual(compound(node.declarators[0]), 0)

    def expression(self, code):
        return self.parser(code).parse_expression()

    def statement(self, code):
        return self.parser(code).parse_statement()

    def parser(self, code):
        return javalang.parser.Parser(
            javalang.tokenizer.tokenize(code)
        )

if __name__ == '__main__':
    unittest.main()
