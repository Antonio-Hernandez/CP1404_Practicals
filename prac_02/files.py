name = input("Please enter a name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
sum_number = number1 + number2
print(sum_number)
in_file.close()

in_file = open('numbers.txt', 'r')
total = 0
for i in in_file:
    numbers = int(i)
    total += numbers
print(total)
in_file.close()
