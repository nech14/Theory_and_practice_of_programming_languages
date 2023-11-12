import pytest
from interpreter import ast, Token, TokenType


class TestAst:

    def test_number_str(self):
        assert ast.Number(Token(TokenType.NUMBER, '1')).__str__() == "Number (Token(TokenType.NUMBER, 1))"

    def test_bin_op_str(self):
        assert ast.BinOp(ast.Number(Token(TokenType.NUMBER, '1')),
                         Token(TokenType.OPERATOR, '%'),
                         ast.Number(Token(TokenType.NUMBER,
                                          '2'))).__str__() == "BinOp% (Number (Token(TokenType.NUMBER, 1)), Number (Token(TokenType.NUMBER, 2)))"

    def test_sign_op_str(self):
        assert ast.SignOp(Token(TokenType.OPERATOR, '-'), ast.Number(
            Token(TokenType.NUMBER, '1'))).__str__() == 'SignOp- Number (Token(TokenType.NUMBER, 1))'

    def test_empty(self):
        assert ast.Empty().__str__() == "Empty"

    def test_variable(self):
        assert ast.Variable("x").__str__() == "Variable(x)"

    def test_assignment(self):
        assert ast.Assignment(ast.Variable("x"), ast.Number(Token(TokenType.NUMBER, '1'))).__str__() == "Assignment(Variable(x) = Number (Token(TokenType.NUMBER, 1)))"

    def test_line_op(self):
        assert ast.LineOp(ast.Empty(), ast.Empty()).__str__() == "LineOp(Empty, Empty)"