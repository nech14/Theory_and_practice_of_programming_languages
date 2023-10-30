import pytest
from interpreter import Interpreter
from interpreter import interpreter as inter
from interpreter import ast, Token, TokenType


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4

    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("t+2")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    def test_invalid_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("-)3")

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            inter.Interpreter.visit_binop(self,
                ast.BinOp(ast.Number(Token(TokenType.NUMBER, '1')),
                          Token(TokenType.OPERATOR, '%'),
                          ast.Number(Token(TokenType.NUMBER, '2'))))

    def test_invalid_token_order(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("-)3")

    def test_invalid_sign(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("*1")

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2 + 2"),
                              (interpreter, "2 +2 "),
                              (interpreter, " 2+2"),
                              (interpreter, " (1+1)*2 "),
                              (interpreter, " 2*2*1 "),
                              (interpreter, " --2*2 "),
                              (interpreter, " +8/2 ")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

    def test_visit_method(self):
        visitor = inter.NodeVisitor()
        result = visitor.visit()
        assert result is None
