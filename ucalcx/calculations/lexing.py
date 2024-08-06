import re
from enum import Enum


class TokenType(Enum):
    CONVERSION = re.compile(r'(->)|(as)|(to)')
    INTEGER = re.compile(r'([0-9])+')
    EQUALS = re.compile(r'=')
    ADD_OP = re.compile(r'(\+|-)')
    RPAR = re.compile(r'\)')
    LPAR = re.compile(r'\(')
    LITERAL = re.compile(r'([a-zA-Z_\-]+)')


class Token:
    def __init__(self, type: TokenType, value: str):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def get_next_token(self) -> Token:
        if self.pos >= len(self.text):
            return None
        else:
            self.current_char = self.text[self.pos]
        
        if self.current_char.isspace():
            self.pos += 1
            return self.get_next_token()

        for token_type in TokenType:
            match = token_type.value.match(self.text, self.pos)
            if match:
                self.pos = match.end()
                return Token(token_type, match.group(0))
        

