# Recursion - these are like function

'''
it is the process of defining something in terms of itself

calling a function inside its own function is Recursive function
'''

# for example:

# lets find out using factorial program

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # calling the same function here again but with different parameters
    
print(factorial(3))

# explanation / dry run
'''
step 1 :
3 will pass to factorial function

step 2:
if condition gets falsed as it is not 1 or 0, goes to else, 
where it will return 3 * factorial(3-1), which is 3 * factorial(2)
here now the function is called again but with different parameters will go back to function

steo 3:
if condition again gets falsed as it is not 1 or 0, goe to else,
where it will return 2 * factorial(2-1), which is  3 * 2* factorial(1) 
here now the function will go back with another different argument

step 4:
now if condition gets true as it is 1, and it will return 1, means in the end it will be 3*2*1 = 6

'''

# ------------------------------- NOTES BY AI ---------------------------

# ---------------------- RECURSION ----------------------

# Recursion → process of solving a problem by calling the same function again

'''
Definition:
A function that calls itself is called a Recursive Function
'''

# Important Parts of Recursion:

# 1. Base Case → condition where recursion stops
# 2. Recursive Case → function calls itself with smaller input


# ---------------------- EXAMPLE: FACTORIAL ----------------------

def factorial(n):
    if n == 0 or n == 1:     # Base case
        return 1
    else:
        return n * factorial(n-1)   # Recursive call

print(factorial(3))
# Output → 6

'''
Correct Dry Run (Step-by-Step)

Your idea was correct, just cleaning it:

factorial(3)
= 3 * factorial(2)

factorial(2)
= 2 * factorial(1)

factorial(1)
= 1   (base case reached)

Now returning back:

factorial(2)
= 2 * 1 = 2

factorial(3)
= 3 * 2 = 6

RULE:
1. Every recursive function must have a base case
2. Input should move towards base case
3. Otherwise → infinite recursion (error)
'''
