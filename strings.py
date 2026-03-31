# STRINGS - are immutable, you can not change

a = 'iamjain'   
# you can not change the above string now 
# but can create another variable using the above variable and the changes you made using methods 


name = 'ujjwal'

# multi_Line_string

string1 = '''
ujjwal jain
also
i am
24 years old
'''
print(string1)

# Indexin in strings - strings are sequence of character so indexing is workable on this

string2 = 'name'
# it will print 'n' as it is on index
print(name[0])


# ----------------------------------------------------------
# For multi line string - will work
# for char in string1:
#     print(char[0]) -> indexing is the reason, why?

# cause indexing is pointless in the loop as it is always one character in the loop but it will still work 

# For multi line string - will work and correct approach
for char in string1:
    print(char)


# ----------------------------- Slicing-----------------------------
name1 = 'i am ujjwal jain'
print(len(name1))

# this works
print(name1[0:2])

# this works cause it will by default take 0 in [:2]
print(name1[:2])

# negative slicing

# it means as - name1[0:len(name1) - 6]
# by default there is len() before the indexing

# both are same and works 0 is by default
print(name1[:len(name1)-6])
print(name1[:-6])

# here same thing will happen as len() func is by default will be before indexing
# this indexing will work

#  when doing negetive indexing like below before indexing should be lower than the after indexing like below
print(name1[-6:-2])


# reverse a string

# [::-1] means 
# start = default
# end   = default
# step  = -1 -> backwards or 1 -> forward


print(name1[::-1])

# -------------------------- string methods---------------------------------

str1 = 'Python learning!!!!!!!'
# 1. upper()
print(str1.upper())

# 2. lower()
print(str1.lower())

# 3. rstrip() - it strip a trailing(Characters at the end (right side) of the string) character
# rstrip() removes characters from the right side of the string.
# rstrip() removes characters until it finds a different character.

str2 = "hello!!!wow!!"
print(str2.rstrip('!')) # hello!!!wow

#  lstrip() Removes left side characters. 
str4 = "!!!hello"
print(str4.lstrip('!'))
#  strip() Removes both side characters.
str3 = "!!!hello!!!"
print(str3.strip('!'))

# 4. replace() - replace all occurenece of a string with another string
print(str1.replace('Python','data analysis').strip('!'))

# 5. split()
str1 = str1.strip('!')
print(str1.split())

# 6. capitalise() - TURNED FIRST LETTER OF THE STRING TO UPPER OTHER TO LOWER
str01 = 'pYTHDOn learn'
print(str01.capitalize())

# 7. center() - align the string to the center as per the parameter
print(str01.center(50))
print(len(str01.center(50)))
print(len(str01))

# 8. count() - count the appearence of the value within the string
str_count = 'python is love is my favourite or is it not it is depend'
print(str_count.count('is'))

# 9. endswith() - checks if the given string ends witjh given value
# gives result in false and true
str_end = 'python is not love!-' 
print(str_end.endswith('!'))

# in between string
print(str_end.endswith('is',4,10)) #check between index 4 to 10 whether the value is ends with or not

# 10. find() - search for the occurence of the given value and returns its index and if givne value is absent from the string then return -1
# 11. Index() - similar to find() but raise error instead of return -1
 
str_find = 'Hi i am ujjwal, my name is ujjwal, my self is ujjwal'
print(str_find.find('ujjwal')) #return the index
print(str_find.find('Ujjwal')) #returne -1 as the string is not matched
# print(str_find.index('Ujjwal'))

# 12. isalnum()- returns true if the string is alpha numaric means 
# between A-Z, a-z, 0-9, is present then true other than that any thing present it returns false

print("Python123".isalnum())   # True
print("Python 123".isalnum())  # False (space present)
print("Python!".isalnum())     # False

# 13. aplha() - returns true if the string is alpha means 
# Returns True if all characters are alphabet letters only (A-Z, a-z)
# Numbers, spaces, and special characters are not allowed

print("Python".isalpha())      # True
print("Python123".isalpha())   # False
print("Python Code".isalpha()) # False (space present)

# 14. islower() - checks if the string is in lower case and if its true returns true else false
str_lower = 'python love' #true
str_lower2 = 'Python love' #false
print(str_lower.islower())
print(str_lower2.islower())

# 15. isupper() - checks if the string is in UPPER case and if its true returns true else false
str_upper = 'PYTHON' #true
str_upper2 = 'Python love' #false
print(str_upper.isupper())
print(str_upper2.isupper())

# 16. isprintable() - checks if the string is printable and returns true and if not then return fales
str_print = 'Python Love' #true
str_print2 = 'Python love\n' #false
print(str_print.isprintable())
print(str_print2.isprintable())

# 17. isspace() -returns true if the string contains only white spaces else return false
# Returns True if the string contains only whitespace characters
# whitespace includes space, tab, newline

print("   ".isspace())         # True
print(" \t ".isspace())        # True
print(" a ".isspace())         # False

# 18. istitle() - returns true if the first letter of each wordd of the string is upper or not
str_title = 'Python Love' #true
str_title2 = 'Python love' #false
print(str_title.istitle())
print(str_title2.istitle())

# 19. startswith() - just like endswith it checks the occurence of the value whther it starts with that value or not and returns true or false
# Checks if the string starts with a given substring
str_start = 'python is love'
print(str_start.startswith("python"))   # True
print(str_start.startswith("java"))     # False

# 20.swapcase() - convert the lower to upper case and upper to lower case
str_swap = 'Python, IS your LOve'
print(str_swap.swapcase())

# 21. title() - capitalise each letter of the word in the string

str_title = 'python is my love'
print(str_title.title())

# 22. isdigit()
# Returns True if all characters are digits (0-9)

print("12345".isdigit())       # True
print("123a".isdigit())        # False
print("123 45".isdigit())      # False (space present)


# 23. isnumeric()
# Similar to isdigit() but slightly more powerful
# It also recognizes numeric characters like fractions or unicode numbers

print("12345".isnumeric())     # True
print("½".isnumeric())         # True
print("123a".isnumeric())      # False


# QUICK VISUAL
# isalnum  → letters + numbers
# isalpha  → letters only
# isdigit  → numbers only
# isnumeric → numbers (including special numeric symbols)
# isspace  → spaces/tabs/newlines