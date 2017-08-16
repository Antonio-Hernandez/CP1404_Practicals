"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_input = False

while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Can't divide by 0")
            continue
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers.txt!")
        # except ZeroDivisionError:
        #     print("Cannot divide by zero!")
print("Finished.")

# Question 1 - A ValueError will occur when entering a string in a int(input()).
# Question 2 - A ZeroDivisonError will occur when you try to divide by zero.
# Question 3 -
