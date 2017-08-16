"""Antonio Hernandez"""


def main():
    username = get_username()
    print_parts(username, 3)


def print_parts(name, step):
    """Display every 'step' character of name."""
    print(name[::step])


def get_username():
    username = input("Please enter a username: ")
    while username == "":
        username = input("Invalid username. Please enter a username: ")
    return username


main()
