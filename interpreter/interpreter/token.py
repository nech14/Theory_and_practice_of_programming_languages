from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    EOL = auto()
    LPAREN = auto()
    RPAREN = auto()

    BEGIN = auto()
    END = auto()
    ID = auto()
    ASSIGN = auto()
    DOT = auto()
    END_LINE = auto()


class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f"Token({self.type_}, {self.value})"
