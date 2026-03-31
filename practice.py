# Q1. Write a Python program that analyzes a string and counts different types of characters.


s = 'Python3.12 is Awesome!!!'

vowels = ['a','e','i','o','u']

f_dict ={'vowels': 0, 'consonant': 0, 'digit' : 0, 'spaces' : 0, 'special':0}
s = s.lower()

for char in s:
    if char in vowels:
        f_dict['vowels'] += 1
    elif char.isalpha():
        f_dict['consonant'] +=1
    elif char.isdigit():
        f_dict['digit'] += 1
    elif char == ' ':
        f_dict['spaces'] +=1
    else:
        f_dict['special'] +=1

print(f_dict)

# Using defaultdict

from collections import defaultdict

s = "Python3.12 is Awesome!!!".lower()

vowels = ['a','e','i','o','u']

counts = defaultdict(int)

for char in s:

    if char in vowels:
        counts['vowels'] += 1

    elif char.isalpha():
        counts['consonants'] += 1

    elif char.isdigit():
        counts['digits'] += 1

    elif char == ' ':
        counts['spaces'] += 1

    else:
        counts['special'] += 1

print(counts)

# --------------------------------------------------

# Q2 Write a Python program that returns the characters that appear **only once** in a string.

S2 = 'programming'

f_d = {}

for char in S2:
    if char not in f_d:
        f_d[char] = 1
    else:
        f_d[char] += 1

app_once = []    


# here c,v are the items gets checked
for c,v  in f_d.items():
    if v > 1:
        pass
    else: 
        app_once.append(c)

print(f_d)
print(app_once)

         
# ---------------------------------------------------------------

# Q3 Write a Python program that finds the **character with the highest frequency** in a string. 

S3 = "mississippi"

f_dict2 = {}
max_c= ''
max_v = 0

for char in S3:
    if char not in f_dict2:
        f_dict2[char] = 1
    else:
        f_dict2[char] +=1

for c,v in f_dict2.items():
    if v > max_v:
        max_v = v
        max_c = c
    else:
        pass
print(max_c,max_v)

# -------------------------------------------------------------------------

# Q4 Write a Python program that **groups characters by their frequency**.

S4 = 'BaNanA'

S4 = S4.lower()

f_dict3 = {}
for char in S4:
    if char not in f_dict3:
        f_dict3[char] = 1
    else:
        f_dict3[char] +=1
    
r_freq = {}
for c,v in f_dict3.items():
    if v not in r_freq:
        r_freq[v] = [c]
    else:
        r_freq[v].append(c)

print(f_dict3)
print(r_freq)



# -------------------------------------------------------------------------
# Write a Python program to count the frequency of each word in a sentence.

S5 = "python is powerful and python is easy"

S5 = S5.split()

f_dict4 = {}

for char in S5:
    if char not in f_dict4:
        f_dict4[char] = 1
    else:
        f_dict4[char] +=1
 
print(f_dict4)

# ---------------------------------------------------------------------------
# Q6 Write a Python program that counts word frequency and then sorts it by frequency in descending order.

s6 = 'data science data engineering data analytics'.split()

f_dict5 = {}

for char in s6 :
    if char not in f_dict5:
        f_dict5[char] = 1
    else:
        f_dict5[char] += 1

sorted(f_dict5.items(), key = lambda x: x[1], reverse=True)

print(f_dict5)