'''
lambda functions are like def function but simpler and shorter 

it will perform same as function, but it is anonumous function with out a name
it is defined using the lambda keyword,

it is often used in situations where a small functions is required a short period of time
Commonly, used as arguments for higher order function such as map, filter and reduce

best use - what if we have to make mini functions in our larger program, it is best to use

'''

# Normal function
def sum(a,b):
    sum = a+b
    return sum

print(sum(6,5))

# lambda function
sum = lambda x,y: x+y
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(sum(6,5))
print(cube(4))
print(avg(10,20))


# Passing function as argument into another function
'''
here i put the function cube i made using lambda as argument
this will call the function in returning stage and return it back to print statement 
'''
def app(fx, value):
    return 6+fx(value)

print(app(cube,2))
# or, just return the lambda functuon directly as arguments
print(app(lambda x: x*x*x,2))


# it can include multiple statement but are limited to a single expression

'''
In this example, the lambda function include print statement, but it is still limited to a single expression
'''
lambda x,y :print(f"{x} + {y} = {x+y}")
