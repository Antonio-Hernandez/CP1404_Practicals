def main():
    numbers_list = []
    for i in range(5):
        numbers = int(input("Numbers: "))
        numbers_list.append(numbers)
    print("The first number is {}".format(numbers_list[0]))
    print("The last number is {}".format(numbers_list[-1]))
    print("The smallest number is {}".format(min(numbers_list)))
    print("The largest number is {}".format(max(numbers_list)))
    print("The average of the numbers is {}".format(sum(numbers_list)/len(numbers_list)))

main()
