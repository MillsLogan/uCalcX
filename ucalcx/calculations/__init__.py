from .parsing import Parser
from .lexing import Lexer
from .interpreter import Interpreter


__all__ = ["Parser", "Lexer", "Interpreter", "calculate"]

def calculate(input: str):
    lexer = Lexer(input)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    return interpreter.interpret()
