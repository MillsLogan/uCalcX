import re
from enum import Enum

class TokenType(Enum):
    CONVERSION = re.compile(r'(->|to|as)')
    EQUALS = re.compile(r'=')
    LPAREN = re.compile(r'\(')
    RPAREN = re.compile(r'\)')
    NUMBER = re.compile(r'\d+|\d+\.\d+')
    PLUS = re.compile(r'\+')
    MINUS = re.compile(r'\-')
    DIVIDE = re.compile(r'/')
    NEWLINE = re.compile(r'\n')
    WHITESPACE = re.compile(r'\s+')
    IDENTIFIER = re.compile(r'[a-zA-z][a-zA-Z_0-9\-]*')
    EOF = re.compile(r'$')

class Token:
    def __init__(self, type: TokenType, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"
    
    def __str__(self):
        return f"Token({self.type}, {self.value})"
    


class Lexer:
    def __init__(self, text: str | None=None, token_rules: TokenType | Enum = TokenType):
        self.token_rules = token_rules
        self.text = text
        self.current_token = None
        self.current = 0

    def set_input(self, text: str):
        self.text = text
        self.current = 0

    def get_next_token(self) -> Token:
        if self.text is None:
            raise ValueError("No input text")
        if self.current >= len(self.text):
            return Token(TokenType.EOF, "")
        
        for token_type in self.token_rules:
            found_token = token_type.value.match(self.text, self.current)
            if found_token:
                value = found_token.group()
                self.current += len(value)
                if token_type == TokenType.WHITESPACE:
                    return self.get_next_token()
                return Token(token_type, value)

    def __iter__(self):
        return self
    
    def __next__(self):
        token = self.get_next_token()
        if token.type == TokenType.EOF:
            raise StopIteration
        return token
            
            
            


