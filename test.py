from ucalcx.calculations.lexing import Lexer, TokenType
from ucalcx.calculations.parsing import Parser



def test_lexer():
    with open("test_input.ucx", "r") as file:
        text = file.read()
    lexer = Lexer(text)
    parser = Parser(lexer)
    for i in range(6):
        print(parser.parse())




if __name__ == '__main__':
    test_lexer()