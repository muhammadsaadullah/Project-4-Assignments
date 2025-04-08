def main():
    print("Square Number :)")

    x:str = input("Enter a number to Square: ")
    num = float(x)

    res = num**2

    print(f"{num:.1f} squared is {res:.1f}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()