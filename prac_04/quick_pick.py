import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    valid_input = False
    while not valid_input:
        try:
            picks = int(input("How many quick picks?: "))
            if picks <= 0:
                print("Quick pick cannot be zero or less than zero.")
                continue
            print_lottery_tickets(picks)
            valid_input = True
        except ValueError:
            print("Quick pick cannot be a string.")


def print_lottery_tickets(picks):
    for i in range(picks):
        for j in range(NUMBER_PER_LINE):
            random_number = random.randint(MIN, MAX)
            print("{:3}".format(random_number), end=' ')
        print()

main()
