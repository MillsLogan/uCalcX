import sys
import os
sys.path.append(os.path.abspath("."))
import ucalcx as ucx
import curses


def main():
    print("Welcome to ucalcx terminal!")
    print("Type 'exit' at any time to quit.")
    print()
    lexer = ucx.calculations.lexing.Lexer()
    parser = ucx.calculations.parsing.Parser(lexer)
    calculator = ucx.calculations.interpreter.Interpreter(parser)
    while True:
        try:
            equation = input("ucalcx > ")
            if equation == "exit":
                break
            print(calculator.calculate(equation))
        except Exception as e:
            print(e)
            continue


def setup_terminal():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    return stdscr



if __name__ == "__main__":
    setup_terminal()