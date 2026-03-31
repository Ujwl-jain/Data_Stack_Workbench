# if __main__ function

'''
it is a commom idiom used in python to determine wheter the script is being run directly
or being imported as module into another script

it is a built in variable that is automatically set to the name of the current module
'''
# for example
from main_function2 import factorial as f

result = f(5)
print(result)


# this is what inside the module main_function2 :

# basically if __name__ does is if we call this inside a function we created then when we run the code main_function2 it will run normally for it
# but if we run the code by importing this module in another code which is main_function then if__name__ will stop the main_function2 to run it self
# in simple terms __main__ function will make sure that function will only run for the code where that function is gets imported.
# also if we print the __name__ then it will tell you where the code is running from
#  general idea for this is stop the imported function to run along with the code we are importing, this way we can not cause the confusing in the complex programs
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # calling the same function here again but with different parameters
    
print(__name__)

if __name__ == '__main__':
    result = factorial(6)
    print(result)
'''