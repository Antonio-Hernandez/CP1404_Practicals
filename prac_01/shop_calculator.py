item_total_price = 0
number_of_items = int(input("Number of Items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of Items: "))

for i in range(number_of_items):
    item_price = float(input("Price of Item: "))
    item_total_price += item_price

if item_total_price >= 100:
    discount = item_total_price * 0.10
    item_total_price -= discount
print("Total price of", number_of_items, "items is", "${:.2f}".format(item_total_price))
