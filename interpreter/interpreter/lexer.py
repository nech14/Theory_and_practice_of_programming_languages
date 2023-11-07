from .token import Token, TokenType

class Lexer():

    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]

    def forward(self):
        self._pos += 1
        if self._pos > len(self._text) - 1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def skip(self):
        while (self._current_char is not None and 
               self._current_char.isspace()):
            self.forward()

    def number(self):
        result  = []
        while (self._current_char is not None and 
               (self._current_char.isdigit() or
                self._current_char == ".")):
            result.append(self._current_char)
            self.forward()
        return "".join(result)

    def next(self):
        while self._current_char:
            if self._current_char.isspace():
                self.skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            if self._current_char in ["+", "-", "/", "*"]:
                op = self._current_char
                self.forward()
                return Token(TokenType.OPERATOR, op)
            if self._current_char == "(":
                op = self._current_char
                self.forward()
                return Token(TokenType.LPAREN, op)
            if self._current_char == ")":
                op = self._current_char
                self.forward()
                return Token(TokenType.RPAREN, op)
            if self._current_char == "B":
                op = "" + self._current_char
                for i in range(4):
                    self.forward()
                    if self._current_char is not None:
                        op += self._current_char
                if op == "BEGIN":
                    return Token(TokenType.ANNOUNCERS, op)
            if self._current_char == "E":
                op = ""+self._current_char
                for i in range(2):
                    self.forward()
                    if self._current_char is not None:
                        op += self._current_char
                if op == "END":
                    return Token(TokenType.ANNOUNCERS, op)
            if self._current_char == ":":
                op = "" + self._current_char
                self.forward()
                if self._current_char is not None:
                    op += self._current_char
                    print('ggg', op)
                    if op == ":=":
                        return Token(TokenType.ASSING, op)
            if self._current_char in [".", ";"]:
                op = self._current_char
                return Token(TokenType.DOTS, op)
            if self._current_char is not None and self._current_char.isalpha():
                op = self._current_char
                return Token(TokenType.VARIABLE, op)

            raise SyntaxError("bad token1")
