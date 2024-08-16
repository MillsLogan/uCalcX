from enum import Enum
import re


class Vocabulary:
    NUMBER = re.compile(r"\d+((\.\d+)|(e\d+))?")  # 123, 123.456, 123e4
    ADDOPS = re.compile(r"\+|-") # +, -
    MULOPS = re.compile(r"\*|/") # *, /
    LPAREN = re.compile(r"\(") # (
    RPAREN = re.compile(r"\)") # )
    POW = re.compile(r"\^") # ^
    IDENTFIERS = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*") # x, y, z, x1, y2, z_3
    WHITESPACE = re.compile(r"\s+")
    EOF = re.compile(r"\Z")
    
    @property
    def keywords(self):
        return [
            re.compile(r"sin|cos|tan"), # sin, cos, tan
            re.compile(r"pi|e"), # pi, e
            re.compile(r"sqrt|log|ln"), # sqrt, log, ln
            re.compile(r"abs|ceil|floor"), # abs, ceil, floor
            re.compile(r"min|max"), # min, max
            re.compile(r"to|as|->"), # to, as, ->
        ]

    @property
    def ignore(self):
        return [self.WHITESPACE]
    
    
class Token:
    def __init__(self, value: str, type: str = None):
        self.value = value
        self.type = type
        
    def __str__(self):
        return f"Token({self.value, self.type})"
    
    def __repr__(self):
        return str(self)


class Lexer:
    def __init__(self, vocabulary: Vocabulary):
        self.vcoabulary = vocabulary
        
    def lex(self, input: str) -> list[Token]:
        tokens = []
        while input:
            for pattern in self.vcoabulary.ignore:
                match = pattern.match(input)
                if match:
                    input = input[match.end():]
                    break
            else:
                for pattern in self.vcoabulary.keywords:
                    match = pattern.match(input)
                    if match:
                        tokens.append(Token(match.group(), "KEYWORD"))
                        input = input[match.end():]
                        break
                else:
                    for pattern in self.vcoabulary.__annotations__.values():
                        match = pattern.match(input)
                        if match:
                            tokens.append(Token(match.group(), pattern.pattern))
                            input = input[match.end():]
                            break
                    else:
                        raise ValueError(f"Unexpected character: {input[0]}")
        return tokens
        