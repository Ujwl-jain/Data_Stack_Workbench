# ---------------------------------------------------------------------------------------------------
# Q1. Given a list of words, return a list of words longer than 5 characters, uppercased.

list_word = ["mango", "tomato", "potato", "ice", "water", "colddrinks", "Lemon"]
list_long =[]

for words in list_word:
    if len(words) > 5:
        list_long.append(words.upper())

print(f"List of words longer than 5 characters in uppercase are: {list_long}")

# using list comprehension ->
list_long = [words.upper() for words in list_word if len(words) > 5]

# Read it like plain English:
# ```
# give me words.upper()
# for every words in list_word
# if len(words) > 5


# ---------------------------------------------------------------------------------------------------
# Q2. Remove duplicates from a list while preserving order (no set shortcuts).5

list_rem = ["mango", "mango", "potato", "ice", "water", "colddrinks", "ice"]
list_original =[]

for words in list_rem:
    if words not in list_original:
        list_original.append(words)
        
list_rem = list_original
print(list_rem)



# ---------------------------------------------------------------------------------------------------
# Q3. Transpose a matrix (list of lists) using list comprehension.

matrix = [[1,2],[5,6],[8,9],[0,4]]
transpose = []
for lst in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[lst])
    transpose.append(new_row)

print(transpose)    

# using list comprehension - need to learn this code
transpose_comp = [                              # outer list
            [row[lst] for row in matrix]        # inner list — same as new_row
            for lst in range(len(matrix[0]))    # outer loop
            ]

# Q4. Use list methods: append, extend, insert, remove, pop, sort, reverse, index, count.

list_methods = ['Ujjwal', 'jain', 59, True, False, 'I am ujjwal Jain']
list_methods.append('Mango is a fruit')
list_methods.extend([1,5,2])
list_methods.insert(3, 'Yeahhhh')
list_methods.remove(59)
list_methods.pop(1)
# since sort can not be done cause list contains different data types
# list_methods.sort()
list_methods.reverse()
print(list_methods.index('Yeahhhh'))
print(list_methods.count('Ujjwal'))
print(list_methods)

# Q45 Given a list of sentences, return a list of lists where each inner
#      list contains the individual words of that sentence.
#      Use list comprehension.

'''
understanding:

list of sentence = ['i am', 'ujjwal jain i am', 'you are not ujjwal']

requriement - 
list of list like this = [['i','am'],['ujjwal','jain'...... and so on]]

i will do both using normal listing and comprehension

'''
#  below code there is an extra space in last element of input list, so if we split using (' ') it will count the extra space, 
# while noramlly using split without argument will clean the double space scenario jsut like in list comp version
# Using normal loop approach
list_of_sentence = ['i am', 'ujjwal jain i am', 'you are not ujjwal ']
nexted_list_of_words = []
for sen in list_of_sentence:
    nexted_list_of_words.append(sen.split(' '))

print(nexted_list_of_words)

# Using list comprehension
nexted_list_comp_words = [word.split() for word in list_of_sentence]
print(nexted_list_comp_words)

# Q6. Given a list of numbers, return a new list replacing every number
#      less than 0 with 0 and every number greater than 100 with 100
#      (clamping). Use list comprehension.


'''
Understanding:
list of mumber = [-1,-4,144,451,6,-8,2,300,8]

return a new list replacing every number less than 0 with 0 and greater than 100 with 100 so its like this

if number is negative(-1) convert it to 0 , if number is greater than 100(766) make it 100, while between number as it is

will use both version normal and list comprehension
'''

list_number = [-1,-4,144,451,6,-8,2,300,8]
updated_list = []

for num in list_number:
    if num < 0:
        updated_list.append(0)
        print(f"the {num} is converted to 0")
    elif num>100:
        updated_list.append(100)
        print(f"the {num} is converted to 100")
    else:
        updated_list.append(num)

print(updated_list)
    
# using list comprehension - here the comdition has to be comes first before the loop

updated_list_comp = [0 if num<0 else 100 if num>100 else num for num in list_number]

# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Ternary Comprehension
# -----------------------------------------------------------------------------
# [0 if num < 0 else 100 if num > 100 else num for num in list_number]
#
# Read as:
#   "For each num → give me 0 if negative, 100 if over 100, else keep num"
#
# ┌─────┬───────────┬──────────────────────────────┬────────┐
# │ num │ condition │         which branch?         │ result │
# ├─────┼───────────┼──────────────────────────────┼────────┤
# │ -1  │  -1 < 0   │ first condition true → 0      │   0    │
# │ -4  │  -4 < 0   │ first condition true → 0      │   0    │
# │ 144 │  144 > 100│ second condition true → 100   │  100   │
# │ 451 │  451 > 100│ second condition true → 100   │  100   │
# │  6  │  0≤6≤100  │ both false → keep num         │   6    │
# │ -8  │  -8 < 0   │ first condition true → 0      │   0    │
# │  2  │  0≤2≤100  │ both false → keep num         │   2    │
# │ 300 │  300 > 100│ second condition true → 100   │  100   │
# │  8  │  0≤8≤100  │ both false → keep num         │   8    │
# └─────┴───────────┴──────────────────────────────┴────────┘

---------
# Q7. Write a function chunk_list(lst, size) that splits a list into
#      chunks of given size. Return a list of lists.
#      Example: ([1,2,3,4,5,6,7], 3) → [[1,2,3],[4,5,6],[7]]

def chunk(lst, size):
    chunk_lst= []
    for i in range(0, len(lst), size):
        chunk_lst.append(lst[i:i+size])
    return chunk_lst

result = [1,2,3,4,5,6,7]
print(chunk(result,3))
