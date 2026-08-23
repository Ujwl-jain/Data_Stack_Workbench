
# ---------------------------------------------------------------------------------------------------------
# Q1  Implement a Caesar cipher: shift each letter by k positions, preserve case and non-letters. - explanation in hard_prob.py

str_CC = 'Hello! World$!'
k = 3
str_c = ''
for char in str_CC:
    if char.isdigit():
        pass
    elif char.isalpha() and char.islower():
        char =  chr(((ord(char) - ord('a')) + k) % 26 + ord('a'))
    elif char.isalpha and char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    else:
        char = char

    str_c = str_c + char

print(str_c)


# or - isalpha() is removed cause islower and isupper is indicating that the char is character not digit

str_CC = 'Hello! World$!'
k = 3
str_c = ''

for char in str_CC:
    if char.islower():
        char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    elif char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    str_c = str_c + char

print(str_c)


# -----------------------------------------------------------------------------------------------------------
# Q2  Find all substrings of a string that are palindromes and return them sorted by length.


str_sub = 'Hello'

list_sub = []
for start in range(len(str_sub)):
    for end in range(start+1, len(str_sub) + 1):
        sub = str_sub[start:end]
        if sub == sub[::-1]:
            list_sub.append(sub)
        else:
            pass

sort_sub = sorted(list_sub, key = len, reverse= True)
print(sort_sub)

# Q3  Implement your own version of str.split() and str.join() without using the built-in methods.
str_func = 'hello world-government'
list_string = []

def is_split(deli):
    temp = ''
    for char in str_func:
        if char == deli:
            list_string.append(temp)
            temp = ''
        else:
            temp = temp + char

    list_string.append(temp)
    print(list_string)


def is_join(deli):
    join_string = ''
    for element in range(len(list_string)):
        if element == len(list_string) - 1:
            join_string = join_string + list_string[element]
        else:
            join_string = join_string + list_string[element] + deli

    print(join_string)

is_split(deli = ' ')
is_join(deli = '-')

-------------
# Q4. Write a function text_statistics(text) that returns a dict with:
#      word_count, unique_words, avg_word_length, most_common_word,
#      longest_word, sentence_count (split by . ? !).
#      Use local variables for intermediate calculations.

from collections import Counter

def text_statistics(text):
    # count sentences BEFORE cleaning
    sentence_count = text.count('.') + text.count('?') + text.count('!')
    
    # clean punctuation THEN split
    clean = text.replace('.', '').replace('?', '').replace('!', '')
    words = clean.split()
    
    # all calculations
    word_count       = len(words)
    unique_words     = len(set(words))
    avg_word_length  = sum(len(w) for w in words) / word_count

    # .most_common(1)[0][0] wil return the pair of tuple of key value pair of top 1 where 0 is frist element of list and another [0] is first element of tuple inside the list
    most_common_word = Counter(words).most_common(1)[0][0]
    longest_word     = max(words, key=len)

    return {
        'word_count'      : word_count,
        'unique_words'    : unique_words,
        'avg_word_length' : round(avg_word_length, 2),
        'most_common_word': most_common_word,
        'longest_word'    : longest_word,
        'sentence_count'  : sentence_count
    }

text = "Hello world. How are you? I am fine! Hello again."
print(text_statistics(text))

----------
# Q5. Write a function that compresses a string using run-length
#      encoding. "aaabbbccddddee" → "a3b3c2d4e2".
#      If a character appears once, just write the character: "abc" → "abc"
