
# Q37 [Hard]   Given a list of (item, price) tuples, find the most expensive item without using max().
list_items = [('apple', 30), ('laptop', 80000), ('pen', 10), ('phone', 50000)]

final_list = sorted(list_items, key = lambda x:x[1], reverse = True)
item, price = final_list[0]
print(item,price)

# using for loop
new_item = ''
max_price = 0
for item, price in final_list:
    if price>max_price:
        max_price = price
        new_item = item
    else:
        pass
print(new_item, max_price)

# Q57. Write a function that takes a list of coordinate tuples (x, y)
#      and returns them sorted first by x, then by y, then returns only
#      the unique coordinates (no duplicates). 