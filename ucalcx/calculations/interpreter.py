from .syntax_nodes import *
from .parsing import Parser
from .. import get_all_units, MetricPrefix, Measurement
from ..length.imperial import *
from .lexing import TokenType, Token

class Interpreter:
    def __init__(self, parser: Parser):
        self.parser = parser
        self.variables = {}
        self.units = get_all_units()
        self.current_node = None

    def calculate(self, equation: str):
        self.parser.set_input(equation)
        return self.interpret()

    def interpret(self):
        self.current_node = self.parser.parse()
        self.variables["ans"] = self._visit(self.current_node)
        return self.variables["ans"]
    
    def _visit(self, node: Node):
        if isinstance(node, AssignmentNode):
            return self._resolve_assignment(node)
        elif isinstance(node, ConversionNode):
            return self._resolve_conversion(node)
        elif isinstance(node, ExpressionNode):
            return self._resolve_expression(node)
        elif isinstance(node, TermNode):
            return self._resolve_term(node)
        elif isinstance(node, MeasureNode):
            return self._resolve_measure(node)
        elif isinstance(node, TerminalNode):
            return self._resolve_terminal(node)
    
    def _resolve_term(self, node: TermNode):
        if isinstance(node.value, MeasureNode):
            return self._visit(node.value)
        elif isinstance(node.value, TerminalNode):
            return self._visit(node.value)

    def _resolve_measure(self, node: MeasureNode):
        scalar = self._visit(node.left)
        unit = self._get_unit(node.value)
        return Measurement(scalar, unit)

    def _resolve_expression(self, node: ExpressionNode):
        left = self._visit(node.left)
        operator = node.value.value
        right = self._visit(node.right)
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        
    def _resolve_terminal(self, node: TerminalNode):
        if node.value.type == TokenType.IDENTIFIER:
            return self.variables[node.value.value]
        elif node.value.type == TokenType.NUMBER:
            return float(node.value.value)

    def _resolve_conversion(self, node: ConversionNode):
        left = self._visit(node.left)
        unit = self._get_unit(node.value)
        return left.convert_to(unit) 

    def _resolve_assignment(self, node: AssignmentNode):
        self.variables[node.value.value] = self._visit(node.left)
        return self.variables[node.value.value]
    
    def _get_unit(self, token: Token):
        for unit in self.units:
            if token.value.endswith(unit.name):
                return unit(self._get_prefix_by_name(token.value[:-len(unit.name)]))
        
        for unit in self.units:
            if token.value.endswith(unit.symbol):
                return unit(self._get_prefix(token.value[:-len(unit.symbol)]))
        
    def _get_prefix(self, prefix: str):
        for metric_prefix in MetricPrefix:
            if metric_prefix.symbol == prefix:
                return metric_prefix
            
    def _get_prefix_by_name(self, name: str):
        for metric_prefix in MetricPrefix:
            if metric_prefix.name == name:
                return metric_prefix
        return MetricPrefix.Base
    
