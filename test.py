from ucalcx.calculations.lexing import Lexer, TokenType
from ucalcx.calculations.parsing import Parser
from ucalcx.calculations.interpreter import Interpreter
from ucalcx.length.metric import Meter
from ucalcx import MetricPrefix, Measurement
from ucalcx.length import get_all_units


def test_lexer():
    meter = Measurement(1, Meter())
    kilometer = Measurement(1, Meter(MetricPrefix.Kilo))
    with open("test_input.ucx", "r") as file:
        text = file.read()
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    for i in range(5):
        print(interpreter.interpret())




if __name__ == '__main__':
    test_lexer()