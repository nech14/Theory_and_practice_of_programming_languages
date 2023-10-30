from .token import Token, TokenType
from .lexer import Lexer
from .ast import BinOp, Number, SignOp


class Parser:
    def __init__(self):
        self._current_token = None
        self._lexer = Lexer()
    
    def check_token(self, type_: TokenType):
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
        raise SyntaxError("Invalid factor")

    def term(self):
        result = self.factor()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in ["*", "/"]:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            return BinOp(result, token, self.factor())            
        return result

    def expr(self):
        result = self.term()
        #print('ffff', self._current_token.type_, self._current_token.value)
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            #print('ffff12', self._current_token.type_)
            if self._current_token.value not in ["+", "-"]:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            #print('hghgh', token.value, token.type_)
            result = BinOp(result, token, self.term())
        return result

    def parse(self, code):
        self._lexer.init(code)
        self._current_token = self._lexer.next()
        return self.expr()
