import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        numbers = []
        for j in range(NUMBER_PER_LINE):
            random_number = random.randint(MIN, MAX)
            while random_number in numbers:
                random_number = random.randint(MIN, MAX)
            numbers.append(random_number)
        numbers.sort()
        print(" ".join("{:2}".format(i) for i in numbers))

main()
