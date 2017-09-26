from prac_07.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.50)
    guitar2 = Guitar("Gibson Les Paul", 2008, 2595.79)

    print(guitar1.get_age())
    print(guitar2.get_age())

    print(guitar1.is_vintage())
    print(guitar2.is_vintage())


main()