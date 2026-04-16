# Q27. Write a recursive function to reverse a string.
#      Do NOT use slicing or any built-in reverse method.

'''
My understanding:
recuresice function to reverse a string, cant use slicing or any built in reverse method

logic is:

using slicing other than slicing used for reverse

bascially return the function with str[1:] this will access the item from 1st indexing which is second element till last + str[0]

means,
return(ello) + h
return(ell) + o + h....

using indexing

basciallt if we provide the indexing as len(str1) - 1 and run it till index is < 0,
then return str[index] + function([str,index-1])

means
return str[4] + function[str, 4-1] = return o + function(hello, 3)
return str[3] + function[str,3-1] = return l + function(hello, 2).....
return str[0] + function[str,0-1] = return h + function(hello, -1), there if condition stops the code and it will reverse the return

to reverse it we have to get access of the last item of string and append it and remove it from original string to get new last item each time recursive function called
base case will be stopped after last element is  == str[0] or len(Str) == 1
'''
def reverse_string(str1):
    if len(str1) > 0:
        return reverse_string(str1[1:]) + str1[0]
    else:
        return str1
    

str1 = 'I am Ujjwal Jain'
print(str1[1:])
result = reverse_string(str1)
print(result)


# using Index
def reverse_string_using_index(str1, index):
    if index < 0:
        return "" 
    return str1[index] + reverse_string_using_index(str1, index - 1)
        

str1 = 'hello'
result = reverse_string_using_index(str1, len(str1) - 1)
print(result)

# Q28. Write a recursive function to check if a string is a palindrome.
#      Return True or False. Do not use slicing.

# using calling function in another function
def reverse_string_using_index(str_to_reverse, index):
    if index < 0:
        return "" 
    return str_to_reverse[index] + reverse_string_using_index(str_to_reverse, index - 1)

def  palindrom_checker(str_palindrom):
    reverse_string = reverse_string_using_index(str_palindrom, len(str_palindrom) - 1)
    if str_palindrom == reverse_string:
        return True
    else:
        return False

str1 = 'racecar'
result = palindrom_checker(str1)
if result:
    print(f"Using 1st approach - calling the function inside another function, It is palindrom: {result}")
else:
    print(f"Using 1st approach - calling the function inside another function, It is Not palindrom: {result}")

# using differnet approach - using indexing but not direct

def  palindrom_checker(str_palindrom):
    if len(str_palindrom) <=1:
        return True
    elif str_palindrom[0] != str_palindrom[len(str_palindrom) - 1]:
        return False
    else:
        return palindrom_checker(str_palindrom[0 + 1:len(str_palindrom) - 1])
    

str1 = 'abca'
result = palindrom_checker(str1)
if result:
    print(f"Using 2rd approach(built with no direct indexing but only - : indexing), It is palindrom: {result}")
else:
    print(f"Using 2rd approach(built with no direct indexing but only - : indexing), It is not palindrom: {result}")
print(result)

# using 3rd approcah without direct indexing (:)

def  palindrom_checker(str_palindrom, start, end):
    if start>=end:
        return True
    if str_palindrom[start] != str_palindrom[end]:
        return False
    else:
        return palindrom_checker(str_palindrom,start + 1, end -1)
    

str1 = 'abba'
result = palindrom_checker(str1, 0, len(str1) - 1)
if result:
    print(f"Using 3rd approach(built without direct - : indexing), It is palindrom: {result}")
else:
    print(f"Using 3rd approach(built without direct - : indexing), It is not palindrom: {result}")



# Q29. Write a recursive function `flatten(lst)` that flattens a deeply
#      nested list of lists into a single flat list.
#      Example: [1, [2, [3, [4]]]] → [1, 2, 3, 4]

'''
my understanding:
flat the nexted list to a list
[1, [2, [3, [4]]]] → [1, 2, 3, 4]

def flatten(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
            
    return flat_list 

nested_list = [1, ['string'], [2, [3, [4]]]]
result = flatten(nested_list)
print(f"the flatten list is {result}")

# using pure recursion
def flatten(lst):
    if not lst:       
        return []
    first = lst[0]
    rest = lst[1:]
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    else:
        return [first] + flatten(rest)

# Q30. Write a recursive function to compute x raised to the power n
#      (x^n). Implement it efficiently using the rule:
#      if n is even: x^n = (x^(n/2))^2
#      if n is odd:  x^n = x * x^(n-1)
# Q30. Write a recursive function to compute x raised to the power n
#      (x^n). Implement it efficiently using the rule:
#      if n is even: x^n = (x^(n/2))^2
#      if n is odd:  x^n = x * x^(n-1)

'''
my understanding:
'''

def power(x, n):
    if n == 0:
        return 1
    
    half = power(x, n // 2)
    '''
    #recurisve call-> half = power(3, 6//2) thic call becomes this - power(3,3)
    #recursice call-> half = power(3, 3//2) this call becmomes this-> power(3,1)
    #recursive call-> half = power(3, 1//2) this call becomes this -> power(3,0) - gets 1
    #recursive call-> half = power(3, 0)  this will return 1 as mentioned in if condition

    # Now rest of the prgram needs to be completed for the each recursive call 
    step 1 
    # we go backwards so for (3,0) - returns 1 mentioned in if condition
    
    step 2
    # Now (3,1//2) get a return value from (3,0) = 1, so half = 1 ->
    check below for 1 as n in this call is 1 which is odd, goes in else condition
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half -> 3 *1*1, which returns 3 to the recursive call  (3,3//2)
    
    step 3
    recursive call 2 for (3,3//2) returns from (3,1//2) which is 3
    half = 3
    check below for 3 as n is 3 in this call which is odd, goes in else condition
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half -> 3 *3*3 - 27, returns 27 to recursiv call (3,6//2)
    
    step 4
    now (3,6//2) recursive call get a return vale from (3,3) which is 27
    half = 27

    check for 6 as it is n in this call below, whoch is even so
    if n % 2 == 0:
        return half * half - > 27*27 = 729
    else:
        return x*half*half

    
     '''

    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
x = 3
n = 6
result = power(x,n)
print(result)

# More enhanced version
def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        # Even case: x^n = (x^(n/2))^2
        half = power(x, n // 2)
        return half * half
    else:
        # Odd case: x^n = x * x^(n-1)
        return x * power(x, n - 1)


# Test
print(power(3, 6))   # 729
print(power(2, 0))   # 1
print(power(5, 1))   # 5
print(power(2, 10))  # 1024
print(power(7, 3))   # 343

