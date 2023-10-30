import pytest
from interpreter import Token, TokenType


class TestToken:

    def test_str(self):
        assert Token(TokenType.NUMBER, '1').__str__() == "Token(TokenType.NUMBER, 1)"
