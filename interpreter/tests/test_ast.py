import pytest
from interpreter import ast, Token, TokenType


class TestAst:

    def test_number_str(self):
        assert ast.Number(Token(TokenType.NUMBER, '1')).__str__() == "Number (Token(TokenType.NUMBER, 1))"


    def test_bin_op_str(self):
        assert ast.BinOp(ast.Number(Token(TokenType.NUMBER, '1')),
                          Token(TokenType.OPERATOR, '%'),
                          ast.Number(Token(TokenType.NUMBER, '2'))).__str__() == "BinOp% (Number (Token(TokenType.NUMBER, 1)), Number (Token(TokenType.NUMBER, 2)))"

    def test_sign_op_str(self):
        assert ast.SignOp(Token(TokenType.OPERATOR, '-'), ast.Number(Token(TokenType.NUMBER, '1'))).__str__() == 'SignOp- Number (Token(TokenType.NUMBER, 1))'