from ucalcx.calculations.lexing import Lexer
from ucalcx.calculations.parsing import Parser
from ucalcx.calculations.interpreter import Interpreter


def test_lexer():
    with open("test_input.ucx", "r") as file:
        text = file.read()
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    for _ in range(5):
        print(interpreter.interpret())


if __name__ == '__main__':
    test_lexer()