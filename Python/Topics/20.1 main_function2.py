def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # calling the same function here again but with different parameters
    
print(__name__)

if __name__ == '__main__':
    result = factorial(6)
    print(result)
