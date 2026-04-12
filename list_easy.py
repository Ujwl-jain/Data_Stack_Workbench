# ---------------------------------------------------------------------------------------------------
# Q13   Create a list of squares of numbers from 1 to 10 using list comprehension.

# Normal way
square_list = []
for i in range(1,11):
    square_list.append(i**2)

print(square_list)

# list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)


# ---------------------------------------------------------------------------------------------------
# Q14   Flatten a list of lists into a single list using list comprehension.

list_list = [['my','name'],[1,2],[True, False]]
final_result = [items for lists in list_list for items in lists]
print(final_result)


# ---------------------------------------------------------------------------------------------------
# Q15   Filter all even numbers from a list using list comprehension.

list_num = [2,1,4,1,5,6,2,8,10,54,99,104,32,14]
list_even = []
# normal way
for item in list_num:
    if item % 2 == 0:
        list_even.append(item)
    else:
        pass
print(list_even)

# list comprehension
list_even2 = [items for items in list_num if items % 2 == 0]
print(list_even2)

# ---------------------------------------------------------------------------------------------------
# Q43. Given a list of integers, return two lists: one with positive
#      numbers and one with negative numbers, using list comprehension.

# using list
list_No = [1,4,671,-2,15,-5,-19,2,10,-17,9]
list_n = []
list_p = []
for i in list_No:
    if i >= 0:
        list_p.append(i)
    else:
        list_n.append(i)

print(f'the list of postive number: {list_p} and the list of negative integers: {list_n}')

# using list comprehension
list_pc= [i for i in list_No if i>=0]
list_nc = [i for i in list_No if i<0]

print(f'the list of postive number: {list_pc} and the list of negative integers: {list_nc}')
