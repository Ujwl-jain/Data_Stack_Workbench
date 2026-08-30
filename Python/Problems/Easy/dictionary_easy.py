# ---------------------------------------------------------------------------------------------------
# Q1. Invert a dictionary (swap keys and values). Assume all values are unique.
dict_invert = {'number' : (1,2,3), 'string' : ('a-z','A-Z'), 'bool' : (True, False)}

dict_swap = {}
 
for key,value in dict_invert.items():
    dict_swap[value] = key

print(dict_swap)


# ---------------------------------------------------------------------------------------------------
# Q2. Merge two dictionaries. If keys conflict, keep the value from the second dict.

buy_dict = {'fruits' : 'mangos', 'veggies' : 'potato', 'spices' : 'clove'}
stock_dict = {'fruits' : 3, 'goods': 5, 'spices' : 10}

final_dict = {}

for key,value in buy_dict.items():
    final_dict[key] = value

for key, value in stock_dict.items():
    final_dict[key] = value

print(final_dict)

# using update - learn this
final_dict = buy_dict.copy()
final_dict.update(stock_dict)

print(final_dict)

# using dict unpacking - learn this
final_dict = {**buy_dict, **stock_dict}

print(final_dict)

# ---------------------------------------------------------------------------------------------------
# Q3. Write a function that takes a list of words and returns a
#      dictionary of word lengths: {'word': length}.

def word_count(word_c):
    dict_final = {}
    for word in word_c:
        dict_final[word] = len(word)
    return dict_final

word_c = ['Mango', 'potato', 'sabji', 'yellow', 'ramen'] 
result = word_count(word_c)
print(result)

# ---------------------------------------------------------------------------------------------------
# Q4. Write a function using a dictionary and a lambda with sorted() to
#      return the top N keys by their value.
#      Example: top 3 scoring students from a scores dict.

scores = {'Alice': 92, 'Bob': 78, 'Charlie': 95, 'Diana': 88, 'Eve': 73}
# top 3 → ['Charlie', 'Alice', 'Diana']

final_dict = sorted(scores.keys(), key = lambda x: scores[x],reverse=True)

print(final_dict[:3])
