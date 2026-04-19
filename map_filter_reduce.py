
'''
Map, filter, reduce:
these are built in function in python
they are higher order function as they can take a function as an argument
'''

# MAP
'''
this function applies a function to each element in a sequence and returns a new sequence
containing the transformed elements,

basically just like we perform actions using loops on each iteration this will do the same and perform a function on each iteration
it is specificially works on any iteration
'''

# a normal program using functions
def cube(x):
    return x*x*x

print(cube(2))

#  but we can do better using map, as this is too much to write, this can be done using a one liner
newl = []
l = [12,4,12,1,4]
for item in l:
    newl.append(cube(item))

print(newl)

# using map - it  will perform the same function on each element, 
# it works like how the above code is working, BUT THIS WILL RETURN A MAP OBJECT FOR EFFICENY PURPOSE AND WE CAN CONVERT EASILY IN ANY IETRABLE DATA TYPE
newl = list(map(cube,l))
print(newl)

# here instead passing te function as a argument we can also just pass a lambda function for efficieny purpose
newl = list(map(lambda x:x*x*x, l))
print(newl)

# ------------------------ 
# FILTER
'''
it filter sequence of elements, based on a given predicate(a function that returns a boolen value)
and returns a new sequence containing only the elements that meet the predicate

basically, just like we perform if_else using condition, we perform filter function using predicate based on the boolean values
'''

def filter_f(a):
    return a>=4

l = [12,4,12,1,4]

# this will return the list of elements based on the predicate/condition applied in the function filter_F()
#  this will also return in filter object, convert it in any iterable datatype
filter_function = list(filter(filter_f, l))
print(filter_function)

# filter function using lambda
'''
we can also just pass the lambda function as argument inside filter function instead of pass a function

in the below code we directly pass the predicate to perform on each element in l to check which one is even or odd
whicheve element comes out to be TRUE will be presented in the list else will be thrown out
'''
evens = filter(lambda x: x%2==0, l)
print(list(evens))


# --------------------------- 
# REDUCE
'''
we have to import to use this function

it takes in 2 arguments at a time from the iterable and perfom the giving function for that 2 arguments and returns a single value,

the reduce function applies the function on first 2 elements in the iterable and applies the function to the result and the next element 
and so on, the reduce function returns the final result
'''
numbers = [1,4,51,2,4]
from functools import reduce
def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)

# using lambda - we can also just pass the lambda function as argument inside reduce function instead of pass a function
sum = reduce(lambda x,y : x+y, numbers)
print(sum)

'''
in the above example. the reduce apllies the lambda functuon to the elemetns in the number list
the lambda function adds the two arguments x and y and returns the result, 
the reduce function then applies the function to the result and the next value in the list and so on

the final result is the sum of all elements in the list
'''