# F_string


# string formating - 

# can be done in python using format method.

# for example:

letter = "my name is {} and i am from {}"
country = 'india'
name = 'ujjwal'

# output - my name is ujjwal ad i am from india
print(letter.format(name, country))

# output - my name is india ad i am from ujjwal
# for fixing thia we can do - "my name is {1} and i am from {0}"
# but it is too manaul
print(letter.format(country, name))

# using string formating
text1 = "the amount is {price:.2f}"
print(text1.format(price =49.08211))


'''
there is no problem doing it the above way but
it is not convinient and doing too mch manual work and code
and need to look for which value comes in which place

that is why in python we use f-string
'''

# F-string  
# its like string formating but look likes this:

country = 'india'
name = 'ujjwal'
# here it will populate the value of variable (name and country) in given places only
print(f"my name is {name} and i am from {country}")

# using f-string
price = 49.08211
print(f"the amout is {price:.2f}")

# also can convert a numeric to string
print(type(f"{2*30}"))

# if i want to print the literal line including the curly brasis then use double curly brasis:
print(f"my name is {{name}} and i am from{{country}}")


# ---------------------------- DOC_STRING --------------------------
# it is not a rocket science

"""
this is doc-string but it should be inside a function after the function is created
it is different from comment

it is used to understand a function more clearly, by defining the description of function, method, class or module.

comment is ignored by interprator, but doc string is not
put the doc string just after the defination of a function,class, module, method

comment can not change the output of a program but, doc string can change the output
"""

# for example
def numaric_1(n):
    """
    takes in a number n, returns the square
    """
    print(n**2)

numaric_1(5)
print(numaric_1.__doc__)

# it will not work, as it is not after just defining a function
def numaric_1(n):
    print(n**2)
    """
    takes in a number n, returns the square
    """
numaric_1(5)
print(numaric_1.__doc__)
