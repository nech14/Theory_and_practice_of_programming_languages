import pytest
from interpreter import parser, TokenType


@pytest.fixture(scope="function")
def par():
    return parser.Parser()


class TestParser:
    par = parser.Parser()

    def test_invalid_token(self, par):
        with pytest.raises(SyntaxError):
            par.check_token(TokenType.NUMBER)
