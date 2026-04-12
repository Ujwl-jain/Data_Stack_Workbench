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