def main():
    print("This program adds two numbers")
    num1: str = input("Enter 1st Number:")
    num1: int = int(num1)
    num2: str = input("Enter 2nd Number:")
    num2: int = int(num2)

    result: int = num1 + num2
    print("Sum:" + str(result))

if __name__ == '__main__':
    main()