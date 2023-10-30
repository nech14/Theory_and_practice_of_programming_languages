from .token import Token


class Node:
    pass


class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number ({self.token})"


class BinOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp{self.op.value} ({self.left}, {self.right})"


class SignOp(Node):

    def __init__ (self, sign: Token, number: Node):
        self.sign = sign
        self.number = number

    def __str__(self):
        return f"SignOp{self.sign.value} {self.number}"
