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

    @pytest.mark.parametrize(
        "interpreter, answer, code", [(interpreter,
                                       {}, """
                                            BEGIN
                                            END.
                                            """),
                                      (interpreter,
                                       {'y': 1.0}, """
                                                BEGIN
                                                    y:= (2*2)/4
                                                END.
                                            """),
                                      (interpreter,
                                       {'y': 2.0, 'a': 3.0, 'b': 18.0, 'c': -15.0, 'x': 11.0},
                                       """BEGIN y:= 2; 
                                                    BEGIN 
                                                        a := 3; 
                                                        a := a; 
                                                        b := 10 + a + 10 * y / 4; 
                                                        c := a - b 
                                                    END; 
                                                    x := 11;
                                                END.""")
                                      ]
    )
    def test_pascal(self, interpreter, code, answer):
        assert interpreter.get_vars(code) == answer

    def test_invalid_statement(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.parser._current_token = Token(TokenType.OPERATOR, '+')
            interpreter.parser.statement()

    def test_visit_method(self):
        visitor = inter.NodeVisitor()
        result = visitor.visit()
        assert result is None
