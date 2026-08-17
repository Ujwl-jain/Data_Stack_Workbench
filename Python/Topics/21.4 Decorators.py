# Decorators

# Normal function
def hello():
    print('heloo world')

def add(a,b):
    print(a+b)

hello()

# What decorators do is

'''
Lets suppose we want to provide a message after running a function
at the end of program, in this case we can simply add a print line inside a function
but what if we have multiple functions??
then when decorators comes in handy

Workflow is working as:

once we add @ greet function before a function and call it, then it will decorate it with whatever in the
decorator function, It will take the called function as an argument in te decorator function and processed further

for example: hello() is being used as argument in greet function

add() is beeing used as argument, but since add() is also having there own arguments 
then we need to use args,kwargs to access those arguments inside the argumented function else it will throw an error
'''
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using the function")
    return mfx

@greet
def hello():
    print('heloo world')

@greet
def add(a,b):
    print(a+b)

# Below 2 lines are saming thing
'''
greet(hello)() is doing the same thing as original code by putting @greet and calling a function
'''
hello()
# greet(hello)()

# if we need to pass the arguments then we have to provide:
'''
*ARGS, **KWARGS IN THE DECORATOR. These will take the arguments else it will show an error
'''
add(1,2)