# ---------------------------------------------------------------------------------------------------
# Q1.  Create a list of squares of numbers from 1 to 10 using list comprehension.

# Normal way
square_list = []
for i in range(1,11):
    square_list.append(i**2)

print(square_list)

# list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)


# ---------------------------------------------------------------------------------------------------
# Q2.   Flatten a list of lists into a single list using list comprehension.

list_list = [['my','name'],[1,2],[True, False]]
final_result = [items for lists in list_list for items in lists]
print(final_result)


# ---------------------------------------------------------------------------------------------------
# Q3.   Filter all even numbers from a list using list comprehension.

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
# Q4. Given a list of integers, return two lists: one with positive
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

# Q5. Write a function that takes a list and uses a lambda with sorted()
#      to sort it by absolute value.
#      Example: [-5, 2, -1, 4] → [-1, 2, 4, -5]

'''
MY UNDERSTANDING:
'''

lst = [-5, 2, -1, 4]
result = sorted(lst, key = lambda x: -x if x < 0 else x)
print(result)

# using abs()
# bascially it converts the -5 to 5 and since key will sort on the basis of these values -5 will be back in the list after sortings
lst = [-5, 2, -1, 4]
result = sorted(lst, key = lambda x: abs(x))
print(result)


# Q6. Use list comprehension with a local variable `threshold = 50` to
#      filter a list of scores — keep scores above threshold and double
#      them.

scores = [45, 60, 75, 30, 85, 55]

threshold = 50
final_list = [x*2 for x in scores if x > threshold]
print(final_list)

# Q.7 Write a function using map() and a lambda that takes a list of
#      temperatures in Celsius and returns them converted to Fahrenheit.
'''
My understanding:

basically list of temperature and convert it into fahrenheit

list of temp = [1,2,3,4,5]
fahrenheit = 
'''
def temp_convert(cel):
    fahren = []
    for temp in cel:
        fahren.append((temp * 9/5) + 32)
    return fahren

cel = [32,4,9,12,-5,12,33]
result = temp_convert(cel)
print(f"Before converting to Fahrenheit {cel}, After converting to Faherheit {result}")

# using map:
result_map = list(map(lambda x:(x * 9/5) + 32, cel))
print(f"Before converting to Fahrenheit {cel}, After converting to Faherheit {result_map}")

# modified verson:
#Q8.  from the dict with key value pair as city and temp, fetch the temperatures in celsius and convert it into fahren, and then return the dict with key value pair has city, fahrenheit

def temp_convertor_list(cel):
    list_celv = []
    list_celk = []
    for k,v in cel.items():
        list_celv.append(v)
        list_celk.append(k)
    
    fahren_lst = temp_convert(list_celv)
    return dict(zip(list_celk, fahren_lst))   


def temp_convertor_list_enhanced(cel):
    """Convert dict of city:celsius → city:fahrenheit"""
    # Extract values, convert using map, then zip back with keys
    fahren_lst = temp_convert(list(cel.values()))
    return dict(zip(cel.keys(), fahren_lst))

# or

def temp_convertor_zip(cel):
    list_celv = []
    for k,v in cel.items():
        list_celv.append(v)
    
    fahren_lst = temp_convert(list_celv)
    my_dict = {key: val for key, val in zip(cel.keys(), fahren_lst)}
    return my_dict

def temp_convertor_zip_enhanced(cel):
    """Improved version using dict comprehension (cleanest)"""
    return {city: (temp * 9/5) + 32 for city, temp in cel.items()}
# or

def temp_convertor_enumrator(cel):
    list_celv = list(cel.values())
    list_celk = list(cel.keys())

    fahren_lst = temp_convert(list_celv)
    for i, key in enumerate(list_celk):
        cel[key] = fahren_lst[i]
    
    return cel

def temp_convertor_enumrator_enhanced(cel):
    """Using enumerate - but without modifying original dict"""
    keys = list(cel.keys())
    values = list(cel.values())
    
    fahren_lst = temp_convert(values)
    
    new_dict = {}
    for i, key in enumerate(keys):
        new_dict[key] = fahren_lst[i]
    
    return new_dict

city_temps = {
    'Mumbai':  32,
    'Delhi':   28,
    'London':  15,
    'NewYork': 22,
    'Tokyo':   18
}
# Expected output:
# {'Mumbai': 89.6, 'Delhi': 82.4, 'London': 59.0, 'NewYork': 71.6, 'Tokyo': 64.4}

result = temp_convertor_list(city_temps)
result2 = temp_convertor_zip(city_temps)
result3 = temp_convertor_enumrator(city_temps)
print(f"Using list with zip, Before converting to Fahrenheit {city_temps}, After converting to Faherheit {result}")
print(f"Using Dict with zip,Before converting to Fahrenheit {city_temps}, After converting to Faherheit {result2}")
print(f"Using Enumrator, Before converting to Fahrenheit {city_temps}, After converting to Faherheit {result3}")

# ---------

