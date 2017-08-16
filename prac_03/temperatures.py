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
            fahrenheit = float(input("Fahrenheit: "))
            print("Result: {:.2f} F".format(convert_fahrenheit_to_celsius(fahrenheit)))
        elif choice == "F":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} C".format(convert_celsius_to_fahrenheit(celsius)))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_fahrenheit_to_celsius(celsius):
    return celsius * 9.0 / 5 + 32


main()
