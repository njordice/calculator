import sys


def main():
    try:
        input1 = float(input("Input a number: "))
        methods = ["+", "-", "/", "*", "^"]
        method = input(f"Input a method ({' '.join(methods)}): ")
        if method not in methods:
            raise ValueError

        input2 = float(input("Input another number: "))

    except ValueError:
        sys.exit("Not a valid input")

    if method == "+":
        result = input1 + input2
    elif method == "-":
        result = input1 - input2
    elif method == "/":
        result = input1 / input2
    elif method == "*":
        result = input1 * input2
    elif method == "^":
        result = input1 ** input2

    print(f"Result: {input1} {method} {input2} = {result}")


if __name__ == "__main__":
    main()
