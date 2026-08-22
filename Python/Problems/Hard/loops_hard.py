# Q1.  Write a function that uses loops to implement the Sieve of
#      Eratosthenes to find all primes up to n.
#      Return the list of primes.
'''
Sieve of Eratosthenes:
Start with all numbers 2 to n → assume ALL are prime
Take 2 → mark all multiples of 2 as NOT prime (4, 6, 8, 10...)
Take 3 → mark all multiples of 3 as NOT prime (6, 9, 12...)
Take 5 → mark all multiples of 5 as NOT prime (10, 15, 20...)
Whatever is left unmarked = PRIME!
'''

def prime_number(n):
    prime_lst =[]

    # set all the value as prime = True 
    is_prime = [True] * (n+1)

    # cause 0,1 can never be prime, starts from 2
    is_prime[0] = False
    is_prime[1] = False

    # what this logic does is runs from 2 to n = 101
    # if the prime is True in the list lets say 2 then make all its multiple false
    # second for loop = range(i*2, n+1, i):, range(2*2 = 4, 101 +1 = 102, 2), (start, from 4, stop, 101, step, take step by leaving 1 digit which logically lands at multiple at 2)
    for i in range(2, n+1):
        if is_prime[i] == True:
            for mul in range(i*2, n+1, i):
                is_prime[mul] = False

    # start from 0 is need cause the index in the boolean list starts from 0
    for i,v in enumerate(is_prime, start = 0):
        if v == True:  # or if v:
            prime_lst.append(i)
    return prime_lst

result = prime_number(101)
print(result)

# Q2. Implement bubble sort using nested loops and count the number of swaps made.

# Q3. Find all Armstrong numbers between 1 and 1000 using loops (e.g. 153 = 1³+5³+3³).
