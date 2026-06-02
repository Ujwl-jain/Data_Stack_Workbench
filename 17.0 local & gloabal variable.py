
# Global Variable
'''
it is defined outisde the function
it can be accessed in any function throughtout the program
'''
# for example:
x = 4 #-> gloabal variable
print(x)

def number():
    # since no variable named x is inside the function 
    # print will print the varaible x which is gloablly available with in the program
    print(f"This is Global Varaible {x}")
number()

# local variable
'''
this defined within the function and is only accessible within that function,
it is created when the function is called and is destroyed when function returns
means local variable use is only with in the prgram

any local vraible used outside the function will not worked, that varaible will only worked within that function or when we called that function 
for example:
'''
x = 4  #-> gloabal variable
print(x)
def number():
    x = 6 #-> local variable
    y = 1 #-> local variable
    # it will priortise the local varable and print it as it is inside the function
    print(f"this is local Varaible {x}")
    print(f"this is local Varaible {y}")

number()
# this will print as it is global variable
print(x)
# -> can not print the value of y as it is only available inside the function and destroyed within it after calling the function
# print(y)


# global keyword
'''
it is used within the function to declare that the variable is global and  should be accessed from the global scope
it is generally not recommneded and a good practice to avoid modifying the global avariable from within the function, as it can lead to unexpected behaviour and harder to debug
better to build a program which does not create a situation to change the vale of global within function
for example:
'''
x = 4  #-> gloabal variable
print(f"this is global variable {x}")

def number():
    global x
    x = 6 #-> local variable, but since we are using global keyword this wll change the value of gloablly variable x with in the program
    y = 1 #-> local variable
    print(f"this is local Varaible {x}")
    print(f"this is local Varaible {y}")

number()
# prints 5
print(f"this is global variable after its get changed within function {x}")

