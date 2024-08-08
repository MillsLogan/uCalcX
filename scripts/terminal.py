import sys
import os
sys.path.append(os.path.abspath("."))
print(sys.path)
import ucalcx as ucx


def main():
    print("Welcome to ucalcx terminal!")
    print("Type 'exit' at any time to quit.")
    print()
    while True:
        try:
            equation = input("ucalcx > ")
            if equation == "exit":
                break
            print(ucx.calculations.calculate(equation))
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()