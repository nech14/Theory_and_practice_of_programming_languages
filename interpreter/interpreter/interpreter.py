from .parser import Parser
from .ast import Number, BinOp, SignOp, Variable, Empty, LineOp, Assignment


class NodeVisitor:
    
    def visit(self):
        pass


class Interpreter(NodeVisitor):


    def __init__(self):
        self.parser = Parser()
        self.variables = dict()


    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, SignOp):
            return self.visit_signop(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, Empty):
            return self.visit_empty(node)
        elif isinstance(node, LineOp):
            return self.visit_lineop(node)
        elif isinstance(node, Assignment):
            return self.visit_assigment(node)


    def visit_assigment(self, node):
        value = 0
        if node.value:
            if isinstance(node.value, BinOp):
                value = self.visit_binop(node.value)
            elif isinstance(node.value, Variable):
                value = self.visit_variable(node.value)
            else:
                value = node.value.token.value
        self.variables[node.var.token] = float(value)

    def visit_empty(self, node):
        return ''

    def visit_variable(self, node):
        return self.variables[node.token]

    def visit_lineop(self, node):
        self.visit(node.left)
        self.visit(node.right)


    def visit_number(self, node):
        return float(node.token.value)


    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")


    def visit_signop(self, node):
        match node.sign.value:
            case "+":
                return self.visit(node.number)
            case "-":
                return -self.visit(node.number)
            case _:
                raise ValueError("Invalid sign")


    def eval(self, code):
        tree = self.parser.parse(code)
        return self.visit(tree)

    def get_vars(self, code):
        self.eval(code)
        return self.variables


