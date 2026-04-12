# Q40 [Medium] Count word frequency in a sentence and return the top 3 most common words.
str_count = 'I am ujjwal jain, and I am 24 years old, i am in love with love python, studies, and games'

dict_freq = {}
count_k = 0

for word in str_count.lower().split():
    if word not in dict_freq:
        dict_freq[word] = 1
    else:
        dict_freq[word] += 1
dict_sort = sorted(dict_freq.items(), key = lambda x:x[1], reverse = True)

print(dict_sort[0:3])

# Q41 [Medium] Group a list of words by their first letter using a dictionary.

str_word = 'Data Scine, data analyst, data validation is the course of my direction value of this certification are vaybig'

dict_group = {}
for words in str_word.lower().split():
    if words[0] not in dict_group:
        dict_group[words[0]] = [words]
    else:
        dict_group[words[0]].append(words)

print(dict_group)

'''
first step is to excess the string convert it into list of words using split doing lower as well
second step is to excess that list and put the words in a list of words in that dictonary as value and its first char as key
for exmple if the word is data {'d' : [data]},
now how to append into the same list into dictonary, if the first word is same using if else
if word.split()[0] not in dict_group, then add it with the list of its value
else:
append in the value of list if it exist 
'''


# Q48. Given a list of transactions as dicts with 'name' and 'amount',
#      calculate the total amount spent per person.
#      Return as a dictionary {name: total}. DONE

def transcation(banking):
    final_dict = {}
    for current_dict in banking:
        name = current_dict['name']
        amount = current_dict['amount']
        if name not in final_dict:
            final_dict[name] = amount
        else:
            final_dict[name] += amount

    return final_dict

banking = [
    {'name': 'Ujjwal', 'amount': 500},
    {'name': 'Rahul',  'amount': 300},
    {'name': 'Ujjwal', 'amount': 200},
    {'name': 'Rahul',  'amount': 100},
    {'name': 'Priya',  'amount': 400},
]
result = transcation(banking)
print(result)

# Q49. Write a function that takes two dicts and returns a dict of keys
#      that are common to both, with a tuple of their values.
#  Example: {'a':1,'b':2}, {'b':3,'c':4} → {'b': (2, 3)} DONE

def dict_filter(a,b):
    filter_dict = {}
    for k,v in b.items():
        if k in a:
            filter_dict[k] = (a[k],v)
        else:
            pass
    
    return filter_dict

dict1 = {'name': 'Ujjwal', 'Human': 'No', 'Class' : 'No class'}
dict2 = {'name': 'Karan', 'Age': 24, 'Class' : 'Interview'}
result = dict_filter(dict1, dict2)
print(result)