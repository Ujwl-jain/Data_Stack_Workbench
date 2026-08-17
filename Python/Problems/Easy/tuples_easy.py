# ---------------------------------------------------------------------------------------------------
# Q33    Unpack a tuple of (name, age, city) and print each using f-strings.

tuple_unpack = ('Ujjwal', '24', 'Pune')
name, age, city = tuple_unpack

print(f"I am {name}, i am {age} year old and i am currently living in {city}")


# ---------------------------------------------------------------------------------------------------
# Q34    Swap two variables using tuple packing/unpacking in a single line.

x = 100
y = 10

x,y = (y,x)

print(y,x)

# -------------------------------------------------------------------------------------------------
# Q55. # Write a function that takes a list of numbers and returns a tuple
#      of (min, max, sum, average) of the list.

# we can not append multiple elements together, need to do one by one, instead use extend()
def calculator(*numbers):
    cal_list = []
    sum = 0
    # a safety check just in case i sent a string for fun
    for n in numbers:    
        sum = sum + n

    avg = sum/len(numbers)
    cal_list.append(min(numbers))
    cal_list.append(max(numbers))
    cal_list.append(sum)    
    cal_list.append(avg)

    return tuple(cal_list)
result = calculator(5,10,2,51,24,12)
print(f"the result for this problem is {result}, and the type of result is {type(result)}")

# More enhaned version
# here if you return multiple things in bracket using comma separated it will return as tuple 
# even if bracket is not there and return is comma separated it will still return as tuple
def calculator(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return (min(numbers), max(numbers), total, avg)

result = calculator(5, 10, 2, 51, 24, 12)
print(f"Result: {result}, Type: {type(result)}")

# Q37. Write a function that takes a list of (name, age) tuples and uses
#      a lambda with sorted() to return them sorted by age ascending.

'''
MY UNDERSTANDING:

take a list of tuple containing the data of name, age pair and use lambda to sort the data using age ascending
means
list of tuples: [(A,15),(B,12)]

sorted = [(B,12), (A,15)]
'''

# using without lambda
def tup_sorting(lot):
    lot_sort = lot
    for ele in range(len(lot) - 1):
        for age in range(len(lot) - 1 - ele):
            if lot_sort[age][1] > lot_sort[age + 1][1]:
                lot_sort[age], lot_sort[age+1] = lot_sort[age+1], lot_sort[age]

    return lot_sort

lot = [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('Diana', 28)]
result  = tup_sorting(lot)
print(f'the result of sorting using age {result}')

# using lambda
lot_sort = sorted(lot, key = lambda lot:lot[1])
print(f'the result of sorting using age {lot_sort}')


# Q38. Write a function that zips two lists into a list of tuples, then
#      uses a dict comprehension to convert it into a dictionary.
#      Demonstrate with names and phone numbers.

'''
My understanding:

basically first make a list of tuples by comparing two list pairing the indexing of each list and then convert that tuple into dict
names  = ['Alice', 'Bob', 'Charlie']
phones = ['9876543210', '8765432109', '7654321098']
expected → {'Alice': '9876543210', 'Bob': '8765432109', 'Charlie': '7654321098'}

'''

def zipper(n, ph):
    zipped = list(zip(n, ph))
    dicted = {k:v for k,v in zipped} 
    return dicted

# Test 1 — normal case
names  = ['Alice', 'Bob', 'Charlie']
phones = ['9876543210', '8765432109', '7654321098']
result  = zipper(names, phones)
print(f'the result of zipping for test case 1 {result}')

# expected → {'Alice': '9876543210', 'Bob': '8765432109', 'Charlie': '7654321098'}

# Test 2 — unequal lengths (zip stops at shorter one!)
names2  = ['Alice', 'Bob', 'Charlie']
phones2 = ['9876543210', '8765432109']

result  = zipper(names2, phones2)
print(f'the result of zipping for test case 2 {result}')

# expected → {'Alice': '9876543210', 'Bob': '8765432109'}  ← Charlie dropped!


# Q39. Write a function that takes a tuple of numbers and returns a new
#      tuple with only the even numbers, using a generator expression
#      inside tuple().

'''
my understanding:

basically return the new tuple with only even numbers in it
'''
def even_odd(tup):
    even_tup = []
    for i in tup:
        if i%2 == 0:
            even_tup.append(i)
        
    return tuple(even_tup)


# Test 1 — mixed even and odd
number = (1, 2, 3, 4, 5, 6, 7, 8)
# expected → (2, 4, 6, 8)
result  = even_odd(number)
print(f'the result of even tuple for test case 2 {result}')

# Test 2 — all odd
number2 = (1, 3, 5, 7)
# expected → ()
result  = even_odd(number2)
print(f'the result of even tuple for test case 2 {result}')

# Test 3 — all even
number3 = (2, 4, 6, 8)
# expected → (2, 4, 6, 8)
result  = even_odd(number3)
print(f'the result of even tuple for test case 2 {result}')

