import ast
from typing import List


class CodeExtractor(ast.NodeVisitor):
    def __init__(self):
        self.operations: List[str] = []

    def visit_Assign(self, node: ast.Assign):
        target = ast.unparse(node.targets[0])
        value = ast.unparse(node.value)
        self.operations.append(f"{target} = {value}")
        self.generic_visit(node)

    def visit_Expr(self, node: ast.Expr):
        expr = ast.unparse(node.value)
        self.operations.append(expr)
        self.generic_visit(node)


def extract_operations(code: str) -> List[str]:
    tree = ast.parse(code)
    extractor = CodeExtractor()
    extractor.visit(tree)
    return extractor.operations
