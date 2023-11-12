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

    def __init__(self, sign: Token, number: Node):
        self.sign = sign
        self.number = number

    def __str__(self):
        return f"SignOp{self.sign.value} {self.number}"


class Variable(Node):

    def __init__(self, name: str):
        self.token = name

    def __str__(self):
        return f"Variable({self.token})"


class Assignment(Node):

    def __init__(self, var: Variable, value: Node):
        self.var = var
        self.value = value

    def __str__(self):
        return f"Assignment({self.var} = {self.value})"


class Empty(Node):

    def __str__(self):
        return f"Empty"


class LineOp(Node):

    def __init__(self, line: Node, new_line: Node):
        self.left = line
        self.right = new_line

    def __str__(self):
        return f"LineOp({self.left}, {self.right})"