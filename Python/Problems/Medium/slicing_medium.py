# Q9  [Medium] Given a list, return the middle third of it using slicing.

list_slice = [1,2,3,4,5,6,7,8,9]

list_len = len(list_slice)
one_third = list_len // 3
start_third = one_third
mid_third = one_third * 2
end_third = one_third * 3

print(list_slice[one_third:mid_third])


# ---------------------------------------------------------------------------------------------------
# Q10 [Medium] Check if a string is a palindrome using slicing (no loops).

str1 = 'racecar'
if str1 == str1[::-1]:
    print("it is palindrome")
else:
    print("it is not palindome")

# Q11 [Medium] Rotate a list to the right by k positions using slicing.
'''
my understanding:
rotate the list by position k

so if k = 2
then
list - [1,2,3,4,5] -> [4,5,1,2,3]

means last 2 elements should come first and rest should move to last

logic:
get the accesss of the last 2 elements using [-k:] -> [-2:] -> give [4,5]

extend it in a new list, get the access of the rest of the elements using [:-k] -> [:-2] -> give [1,2,3]

extend it to the new list

but what about the edge case what if k > len(list)
hten why?? k = k % len(lst)
'''


str1 = [1,2,3,4,5]
k = 8
final_result = []
if k > len(str1):
    k = k % len(str1)
    final_result.extend(str1[-k:])
    final_result.extend(str1[:-k])
else:
    final_result.extend(str1[-k:])
    final_result.extend(str1[:-k])

print(final_result)

# enhanced version
lst = [1,2,3,4,5]
k = 2

k = k % len(lst)

final_result = lst[-k:] + lst[:-k]

print(final_result)
