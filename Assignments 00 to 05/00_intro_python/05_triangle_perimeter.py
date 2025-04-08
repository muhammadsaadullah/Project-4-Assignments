def main():
    print("Triangle Preimeter Calc :)")

    side1: str = input("Enter lenght of 1st Side: ")
    side2: str = input("Enter lenght of 2nd Side: ")
    side3: str = input("Enter lenght of 3rd Side: ")

    s1 = float(side1)
    s2 = float(side2)
    s3 = float(side3)

    Peri = s1 + s2 + s3

    print(f"The perimeter of the triangle is {Peri:.1f}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()