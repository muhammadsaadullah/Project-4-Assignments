def main():
    print("Farhan-Height to Celsius :)")

    usrInput: str = input("Enter Temperature in Farhan-Height: ")
    degrees_fahrenheit = float(usrInput)

    degrees_celsius : float = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")




if __name__ == '__main__':
    main()