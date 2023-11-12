from .token import Token, TokenType
from .lexer import Lexer
from .ast import BinOp, Number, SignOp, Empty, Assignment, Variable, LineOp


class Parser:
    def __init__(self):
        self._current_token = None
        self._lexer = Lexer()
    
    def check_token(self, type_: TokenType):
        #print(type_, self._current_token.type_, self._current_token.value)
        if self._current_token and self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError("invalid token order")

    def factor(self):
        token = self._current_token
        if token.type_ == TokenType.NUMBER:
            self.check_token(TokenType.NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPAREN:
            self.check_token(TokenType.LPAREN)
            result = self.expr()
            self.check_token(TokenType.RPAREN)
            return result
        if token.type_ == TokenType.OPERATOR:
            self.check_token(TokenType.OPERATOR)
            return SignOp(token, self.factor())
        if token.type_ == TokenType.ID:
            result = self._current_token.value
            self.check_token(TokenType.ID)
            return Variable(result)
        raise SyntaxError("Invalid factor")

    def term(self):
        result = self.factor()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in ["*", "/"]:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            return BinOp(result, token, self.term())
        return result

    def expr(self):
        result = self.term()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.term())
        return result

    def assignment(self):
        id = Variable(self._current_token.value)
        self.check_token(TokenType.ID)
        self.check_token(TokenType.ASSIGN)
        return Assignment(id, self.expr())

    def empty(self):
        return Empty()

    def statement(self):
        match self._current_token.type_:
            case TokenType.BEGIN:
                return self.complex_statement()
            case TokenType.ID:
                return self.assignment()
            case TokenType.END:
                return self.empty()
            case _:
                raise SyntaxError("Invalid statement")

    def statement_list(self):
        result = self.statement()
        if self._current_token and self._current_token.type_ == TokenType.END_LINE:
            self._current_token = self._lexer.next()
            #result = self.statement_list()
            result = LineOp(result, self.statement_list())
        return result

    def complex_statement(self):
        self.check_token(TokenType.BEGIN)
        result = self.statement_list()
        self.check_token(TokenType.END)
        return result

    def program(self):
        result = self.complex_statement()
        self.check_token(TokenType.DOT)
        return result

    def parse(self, code):
        self._lexer.init(code)
        self._current_token = self._lexer.next()
        print('ffgfg', self._current_token)
        if self._current_token.type_ in [TokenType.NUMBER, TokenType.OPERATOR, TokenType.LPAREN]:
            return self.expr()
        return self.program()
