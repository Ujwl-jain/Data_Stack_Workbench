# Q5.  Write a function `apply_twice(func, value)` that takes another
#      function and a value, applies the function to the value twice,
#      and returns the result. (Higher-order function)



# ----------------------------------------------------------------------------------------------------------------
# Q6.  Write a function `power_factory(exp)` that returns a new function
#      which raises any number to the power `exp`. Use closures.
#      Example: square = power_factory(2); square(5) → 25

def power_factory(exp):
    return square_power(exp, value = 5) 

def square_power(exp, value):
    square = value ** exp
    return square

result = power_factory(2)
print(result)

# or using closure function

def power_factory(exp):
    def square_power(value):
        square = value ** exp
        return square
    return square_power

square = power_factory(2)
cube = power_factory(3) 
fifth = power_factory(5) 
print(square(5))
print(cube(4))
print(fifth(2))


# ----------------------------------------------------------------------------------------------------------------
# Q7.  Write a function that accepts **kwargs and prints each key-value
#      pair in the format "key: value". Then call it with at least 4
#      different keyword arguments.

def kwargs(**pairs):
    for k,v in pairs.items():
        print(f'{k} : {v}')

kwargs(name = 'Ujjwal', status ='single', age = 24, hobby = 'programming', city = 'Pune')


# ----------------------------------------------------------------------------------------------------------------
# Q8.  Write a function `safe_divide(a, b)` that returns the result of
#      a / b, but returns None and prints a warning if b is 0.
#      Demonstrate calling it with both valid and zero divisor.

def safe_divide(a,b):
    if b == 0:
        return None
    return a/b
        
result = safe_divide(a = 6, b = 0)
if result is None:
    print(f"Warning: Invalid Divisor")
else:
    print(result)

# ----------------------------------------------------------------------------------------------------------------
# Q9.  Write a lambda function that takes a list of tuples (name, score)
#      and returns the list sorted by score in descending order.

data = [('alice', 'maths', 85), ('matter', 'english', 98), ('alice', 'ciene', 18), ('matter', 'hindi', 99), ('harry', 'sst', 77), ('DJ', 'sports', 99)]

# this code will male sure to sort the score and name in descending order but in case of tiebreaker name will sort as well to make sure name does not be in descending oreder
final_list  = sorted(data, key = lambda x: (x[2], x[0]), reverse = True)

#  use this : below code is used to make sure name will not be in descending order, In simple terms, '-' before score indexing also means score in descending
#  cause the score then will be in minus like -99, which is auto matically a smaller number and operating will perform in ascending order: -99, -98,-18,-7
# since inside key all elements are used for temperroray basis '-' will be thrown and it will return the same order but with out minus hence sorted in descending, only works on number
# key=lambda x: (-x[2], x[0])  # ← negative score = descending, name stays ascending!
print(final_list)
