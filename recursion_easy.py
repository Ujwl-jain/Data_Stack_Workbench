# Q23. Write a recursive function to compute the factorial of n.
#      factorial(0) = 1, factorial(n) = n * factorial(n-1).
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * factorial(num-1))

result = factorial(5)
print(result)

# Q24. Write a recursive function to compute the nth Fibonacci number.
# fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2). DONE

def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(result)

# using loop + recursion list of fibonacci 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    result = []
    
    for i in range(n+1):
        result.append(fib(i))
    
    return result

print(fibonacci(10))


# Q25. Write a recursive function that computes the sum of all elements
#      in a list without using any built-in sum() function. DONE

def sum_list(list_sum):
    if len(list_sum) == 0:
        return 0
    else:
        total = list_sum[0] + sum_list(list_sum[1:])
        return total

list_sum = [1,2,34,5]
print(sum_list(list_sum))



# Q26. Write a recursive function `count_down(n)` that prints numbers
#      from n down to 0, then prints "Go!".