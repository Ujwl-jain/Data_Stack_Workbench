# How importing works in python

'''
it is a process of loading code from python module into the current code.

this way we can use the functions and vairables defined in the module in our current code
like:
'''
# import pandas
# import numpy
# import os
# import 


'''
Many importing modules has many functions, so have to learn more about them specifically to apply those function
for example:

full syntac = 
import module
module.function_name()
'''

# after importing pandas library we can use its one of the functon read_csv(), 
# read about each function to know about its functionality
# import pandas
# pandas.read_csv()

# example:

import math
math.floor(4.4352)

# this will square root the number 9 output - 3.0 in floot
result = math.sqrt(9)
print(result)

#  -------------- From key word -------------------
# we can also import a specific function directly using a from keyword, for example:
from math import sqrt, pi

# now we domt need to use the math. syntax as we alreadu imprt the function here
result = sqrt(9) * pi
print (result)

# this will import all the functions and variables - not recommended appraoch untill and unless you knwo what you are doing
# from math import *


# ---------------- as keyword -------------------------
# in bigger programs we need to use the module name many times so we can not just write each word again n agaian
#  so we can use as keyword to define a module name - that namy can be anything but recommended to use a sensible name
# for example:
import pandas as pd

# here now we will use the function short name as we define while importing using as keywrod
import math as m
result = m.sqrt(9)
print(result)


from math import pi, sqrt as s
result = s(9) * pi
print(result)

# --------------------- dir function ----------------------
#  lets say we dont kmow any thing about a module
#  then we can use the dir function to print the list of functions included in a module

# for example:
print(dir(math))

# this will give a nan name and its type
print(math.nan, type(math.nan))


# ---------------- custom modules ---------------------

'''
basically it is the process of importing a custom function user has created and use it in our own diferent Code
this can keep things organised and reusability will be increased in complex programming

for example: below i import a function factorial from one of the file recurrsion i created.
    the function will perform the task as defined in the recursion file 
    and return the result in this code which is 120
'''
from recursion import factorial 
result = factorial(5)
print(result)

# from recurrion import factorial as f
# result = f(5)
# print(result)
