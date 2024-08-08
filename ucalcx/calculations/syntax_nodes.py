from .lexing import Token
from typing import Optional, Self, Union


class Node:
    def __init__(self, value: Token, left: Optional[Self]=None, right: Optional[Self]=None,):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return f"{str(self.__class__.__name__)}({self.value}{', ' + str(self.left) if self.left is not None else ''}{', ' + str(self.right) if self.right is not None else ''})"
    
    def __str__(self):
        return f"{str(self.__class__.__name__)}({self.value}{', ' + str(self.left) if self.left is not None else ''}{', ' + str(self.right) if self.right is not None else ''})"


class ConversionNode(Node):
    def __init__(self, unit: Token, scalar: Node):
        super().__init__(unit, left=scalar)

class ExpressionNode(Node):
    def __init__(self, value: Token, left: Optional[Self]=None, right: Optional[Self]=None, ):
        super().__init__(value, left, right)


class AssignmentNode(Node):
    def __init__(self, identifier: Token, expression: ExpressionNode):
        super().__init__(identifier, left=expression)


class TermNode(Node):
    def __init__(self, value: Token, left: Optional[Self]=None, right: Optional[Self]=None):
        super().__init__(value, left, right)


class TerminalNode(Node):
    def __init__(self, value: Union[ExpressionNode, TermNode]):
        super().__init__(value)


class MeasureNode(Node):
    def __init__(self, unit: Token, scalar: TerminalNode):
        super().__init__(unit, left=scalar)
