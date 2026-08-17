# Q52 [Easy]   Format a person's info with f-string: name, age, and salary rounded to 2 decimal places.
name = 'Ujjwal'
age = 24
Salary = 4500.45146

print(f"My name is {name}, My age is {age}, and my salary is {Salary:.2f}")

# Q53 [Easy]   Write a function with a proper docstring that converts Celsius to Fahrenheit.

def doc_string(c):
    '''
    Here the goal is to convert the celsius to Fahrenheit
    basically we can convert it using below formula
    this function will return the F to the caller
    '''
    F = (c * 9/5) + 32
    return F
f = doc_string(14)
print(f)

# enhanced -
def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (c * 9/5) + 32
    return fahrenheit


f = celsius_to_fahrenheit(14)
print(f)
