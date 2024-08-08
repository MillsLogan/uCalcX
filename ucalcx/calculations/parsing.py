from .lexing import Token, TokenType, Lexer
from .syntax_nodes import *


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = None

    def set_input(self, text: str) -> None:
        self.lexer.set_input(text)
        self.current_token = None

    def parse(self) -> Node:
        if self.current_token is None or self.current_token.type == TokenType.NEWLINE:
            self._advance()
            return self.parse()
        if self.current_token.type == TokenType.EOF:
            return None
        return self._statement()
    
    def _statement(self) -> Node:
        if self.current_token.type == TokenType.IDENTIFIER:
            identifier = self.current_token
            self._eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.EQUALS:
                return self._assignment(identifier)
            else:
                left =  self._expression(identifier)
        else:
            left = self._expression()
        
        if self.current_token.type == TokenType.CONVERSION:
            self._eat(TokenType.CONVERSION)
            right = self._terminal()
            return ConversionNode(right.value, left)
        else:
            return left


    def _assignment(self, identifier: Token) -> AssignmentNode:
        self._eat(TokenType.EQUALS)
        expression = self._expression()
        return AssignmentNode(identifier, expression)
    
    def _expression(self, identifier: Optional[Token]=None) -> ExpressionNode:
        if identifier is None:
            left = self._term()
        else:
            left = TerminalNode(identifier)
        
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            operator = self.current_token
            self._eat(self.current_token.type)
            right = self._term()
            left = ExpressionNode(operator, left, right)
        
        return left

    def _term(self) -> TermNode:
        left = self._terminal()
        if left.value.type == TokenType.NUMBER:
            return TermNode(self._measure(left))
        elif left.value.type == TokenType.IDENTIFIER:
            return TermNode(left)
        else:
            raise ValueError(f"Expected number or identifier, got {str(left.value)}")
    
    def _measure(self, scalar: Node) -> Node:
        unit = self.current_token
        self._eat(TokenType.IDENTIFIER)
        return MeasureNode(unit, scalar)
            
        
    def _terminal(self) -> TerminalNode:
        if self.current_token.type == TokenType.NUMBER:
            token = self.current_token
            self._eat(TokenType.NUMBER)
            return TerminalNode(token)
        elif self.current_token.type == TokenType.IDENTIFIER:
            token = self.current_token
            self._eat(TokenType.IDENTIFIER)
            return TerminalNode(token)
        elif self.current_token.type == TokenType.LPAREN:
            self._eat(TokenType.LPAREN)
            expression = self._expression()
            self._eat(TokenType.RPAREN)
            return TerminalNode(expression)
        else:
            raise ValueError(f"Expected number, identifier, or expression, got {str(self.current_token)}")
            
    def _eat(self, token_type: TokenType) -> None:
        if self.current_token.type == token_type:
            self._advance()
        else:
            raise ValueError(f"Expected {token_type}, got {str(self.current_token)}")

    def _advance(self) -> None:
        self.current_token = self.lexer.get_next_token()

        
        



