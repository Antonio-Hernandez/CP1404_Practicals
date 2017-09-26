from prac_07.guitar import Guitar


def main():
    guitars = []

    # print("My guitars!")
    # name = input("name: ")
    # while name != "":
    #     year = input("year: ")
    #     cost = input("cost: ")
    #     guitar_info = Guitar(name, year, cost)
    #     guitars.append(guitar_info)
    #     print("{} ({}) : {} added.".format(name, year, cost))
    #     name = input("name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for number, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f} {2}".format(number + 1, guitar,
                                                                                       vintage_string))


main()
