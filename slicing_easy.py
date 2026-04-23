# ---------------------------------------------------------------------------------------------------
# Q7  [Easy]   Reverse a string using slicing only (no built-in reverse).

str_reverse = 'I am Ujjwal jain'
print(str_reverse[::-1])

# Q8  [Easy]   Extract every other character from a string starting from index 0.
str_cha= 'i am ujjwal jain i am 24 year old'
print(str_cha[::2])

# Q64. Write a function that takes a string and uses slicing to return
#      the first half and second half separately as a tuple.
#      For odd length, the middle character goes to the first half.
'''
my understanding:

string = Ujjwal, divide it in two halfs using slicing, return first halt and second half seperatly as tuple
if its odd len string then return the mid variable to first half.
if its even then its fine

Ujjwalj has 7 words, then (Ujjw, alj)

'''

def divider_string(st):
    if len(st) % 2 == 0:
        first_half = st[:int(len(st)/2)]
        second_half = st[int(len(st)/2):]
        return (first_half,second_half)
    else:
        first_half = st[:(int(len(st)/2) + 1)]
        second_half = st[(int(len(st)/2)) + 1:]
        return (first_half,second_half)
    
st = 'Ujjwal'
result_even = divider_string(st)
result_odd = divider_string('UjjwalJ')
print(f'the result after dividing the string in EVEN CASE is: {result_even}')
print(f'the result after dividing the string in ODD CASE is: {result_odd}')

# enhanced version:
def divider_string(st):
    mid = len(st) // 2
    if len(st) % 2 != 0:
        mid += 1                    
    return (st[:mid], st[mid:])     

print(divider_string('Ujjwal'))   # ('Ujj', 'wal') 
print(divider_string('UjjwalJ'))  # ('Ujjw', 'alJ') 

# Q65. Given a list, use slicing to remove the first 2 and last 2
#      elements. Return the remaining middle portion.

'''
my understanding

list = [1,2,3,4,5,6] -> remove 1,2,5,6 and return [3,4]

remove first 2 and last 2 elemetns and return the remainimg
'''

def divider_list(lst):
    sliced = lst[2:-2]
    return sliced

lst = [1,2,3,4,5,6,7]
result = divider_list(lst)
print(f'the result after dividing the string in ODD CASE is: {result}')


# Q66. Write a function that uses slicing to check if a list is a
#      palindrome (reads the same forwards and backwards).

'''
my understanding:

check whether the list is palindrom or not
so if list = [1,2,3,2,1] 
'''

def palindrome(lst):
    if lst == lst[::-1]:
        return 'it is palindrome'
    else:
        return 'It is not palindrom'
    
lst = [1,2,3,2,1]
result = palindrome(lst)
print(f'{result} cause list = {lst} and reversed list = {lst[::-1]}')
