# TYPECASTING

# conversin of one data type to another is called type casting
# for example int to string 

# Functions which help in conversion:
# int(), str() ,  ord(), hex(), oct(), tuple(), 
# set(), list(),  dict(), etc.

# EXAMPLE:
a ='2'
b ='4'
# it will add the number as it is string
print(a+b)

# it will convert the string into number if possible and add it
#  it should be valid response from user
#  like not name can not be able to convert to integer it is invalid

print(int(a) + int(b))


# ------------------Two types----------------------
# implicit -  it dont have the same level 
#  datatypes may have higher order or lower order 
#  it will automatically change the data type of a result into the higher  order datatype to prevent data loss
#  For example below codes result wlll be in float not int cause float is higher order than int
c = 11.9
d = 10

print(c+d)
 
# explicit- done or initiate by user just like above code example:

string = '15 ' 
b = 5

print("the output for the following code will be:",int(string) + b)