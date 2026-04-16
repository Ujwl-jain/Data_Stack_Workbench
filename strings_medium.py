# Q23 [Medium] Check if two strings are anagrams of each other.

str1 = input("enter the first string: ")
str2 = input("enter the 2nd string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("yes this is anagram")

else:
    print("it is not anagram")


# Q24 [Medium] Find the longest word in a sentence using string methods only.

'''
my understanding:

find the longest words in a sentence usign string methods only

means str = i have so many mangoes, longest number = mangoes

logic
use split on string to convert it into list
apply loop on list, accessing each word,

count that word using len function
'''

str1 = 'i have so many mangos apples'

store = str1.split()
longest_word = ''

for word in store:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)

# incase there are 2 same len varaible then store it in list
str1 = 'i have so many mangos apples'


store = str1.strip(' ').split()
longest_word = []
max_len = 0
for word in store:
    if len(word) > max_len:
        max_len = len(word)
        longest_word.clear()
        longest_word.append(word)
    elif len(word) == max_len:
        longest_word.append(word)
    else:
        pass

print(longest_word)

# using function
def longest_Word(store):
    store = str1.strip(' ').split()
    longest_word = ''
    longest_word_list = []
    max_len = 0
    for word in store:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
            longest_word_list.clear()
            longest_word_list.append(word)
        elif len(word) == max_len:
            longest_word_list.append(word)
        else:
            # if i put return here as return empty list what would happen?
            # return []
            pass    

    # this will return based on the no of words, if 1 longest word return a word, else return the list
    if len(longest_word_list) > 1:
        return longest_word_list
    else:
        return longest_word

str1 = 'i have so many mangos apples '
result = longest_Word(str1)
print(result)

# more enhanced version

def find_longest_words(sentence):
    if not sentence or not sentence.strip():
        return []                    # Handle empty or only spaces
    
    words = sentence.strip().split() # Clean + split (handles multiple spaces)
    
    if not words:
        return []
    
    max_len = 0
    longest_words = []
    
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_words = [word]       # Reset list with new longest
        elif len(word) == max_len:
            longest_words.append(word)   # Add another word with same length
    
    return longest_words


# ==================== Test Cases ====================
print(find_longest_words('i have so many mangos apples'))      # ['mangos', 'apples']
print(find_longest_words('the quick brown fox jumps'))         # ['quick', 'brown', 'jumps']
print(find_longest_words('hello'))                             # ['hello']
print(find_longest_words('   '))                               # []
print(find_longest_words('a bb ccc ddd'))                      # ['ccc', 'ddd']
print(find_longest_words('one two three'))                     # ['three']

# Q25 [Medium] Count frequency of each character in a string and return as a dictionary.

'''
my understanding

count the frequency of a word and return as a dict, means

string = i have store
store = 5 character
dict = {'store' : 5.....}

approach:
1st approach use collection counter directly
2nd use loop and if else to count the word and frequency 

Logic
1st
import counter from collection

apply it on string

print the result
2nd

create an empty dict, create a counter = 1
for loop to process through the string char by char
if char not in dict addit
else increase its value

i will also count digit as char as it is part of string, and string = charcter, '1' = string
'''
# using colletions
from collections import Counter

# test cases
# str1 = 'I have 2 world class batsman in my team'
# str1 = 'aabbcc'
str1 = 'Batsmanb123'
result = Counter(str1.strip())

print(result)


# using normal approch
count = 1
dict_char = {}
for char in str1.strip():
    if char not in dict_char:
        dict_char[char] = count
    else:
        dict_char[char] += count

print(dict_char)

# using functions
def count_using_counter(str1):
    return Counter(str1())

def count_using_manully(str1):
    count = 1
    dict_char = {}
    for char in str1():
        if char not in dict_char:
            dict_char[char] = count
        else:
            dict_char[char] += count
    
    return dict_char


str1 = 'AAbCddba'
print(f'this result is produce using counter library {count_using_counter(str1)}')

print(f'this result is produce using counter library {count_using_manully(str1)}')

# Q40. Write a function that converts a snake_case string to camelCase.
#      Example: "hello_world_python" → "helloWorldPython"

# Q41. Write a function that takes a string and returns True if all
#      brackets are balanced: (), [], {}.
#      Example: "{[()]}" → True,  "{[(])}" → False

