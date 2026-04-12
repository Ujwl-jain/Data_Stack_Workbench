# ---------------------------------------------------------------------------------------------------
# Q16 [Medium] Given a list of words, return a list of words longer than 5 characters, uppercased.

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
# Q17 [Medium] Remove duplicates from a list while preserving order (no set shortcuts).5

list_rem = ["mango", "mango", "potato", "ice", "water", "colddrinks", "ice"]
list_original =[]

for words in list_rem:
    if words not in list_original:
        list_original.append(words)
        
list_rem = list_original
print(list_rem)



# ---------------------------------------------------------------------------------------------------
# Q18 [Medium] Transpose a matrix (list of lists) using list comprehension.

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

# Q59 [Medium] Use list methods: append, extend, insert, remove, pop, sort, reverse, index, count.

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

# Q44. Given a list of sentences, return a list of lists where each inner
#      list contains the individual words of that sentence.
#      Use list comprehension.

# Q45. Given a list of numbers, return a new list replacing every number
#      less than 0 with 0 and every number greater than 100 with 100
#      (clamping). Use list comprehension.
