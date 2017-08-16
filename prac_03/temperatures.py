"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_fahrenheit_to_celsius()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            celsius = convert_celsius_to_fahrenheit()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    return 5 / 9 * (fahrenheit - 32)


def convert_fahrenheit_to_celsius():
    celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32


main()
