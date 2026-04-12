# ---------------------------------------------------------------------------------------------------
# Q21   Count vowels in a string without using any built-in count method.
string_line = 'i am ujjwal jain and i am 24 years old'

# set lookup is faster than list lookup here so instead of list we can create a set as well
# set_vowels ={'a','e','i','o','u'}
list_vowels = ['a','e','i','o','u']
count_v = 0
count_c = 0

for char in string_line.lower():
    if char in list_vowels:
        count_v += 1
    elif char.isalpha():
        count_c += 1
    else:
        pass
print(f"the number of vowels in the string is {count_v} and the number of consonant is {count_c}" )

# built in method approach - need to dry run this again
string_line = 'i am ujjwal jain and i am 24 years old'
vowels = 'aeiou'
count_v = sum(string_line.lower().count(v) for v in vowels)
print("Vowels:", count_v)

# using built in method and list comprehension - dry run this
string_line = 'i am ujjwal jain and i am 24 years old'
vowels = 'aeiou'

# meaning of the below line os  - For every character that satisfies the condition → add 1
# We use 1 because each valid character contributes 1 to the total count
count_v = sum(1 for char in string_line.lower() if char in vowels)
count_c = sum(1 for char in string_line.lower() if char.isalpha() and char not in vowels)

print("Vowels:", count_v)
print("Consonants:", count_c)


# ---------------------------------------------------------------------------------------------------
# Q22   Reverse words in a sentence (not characters).

string_rev = 'i am ujjwal jain and i am 24 years old'
list_rev = string_rev.split()[::-1]

rev_string = ' '.join(list_rev)
print(rev_string)


# -----------------------------------------------------------------------------------------------------
# Q39. Write a function that takes a sentence and returns the number of
#      words, characters (no spaces), and sentences (count periods).

def sen_checker(sen):
    # Splitting by . gives one extra empty string at the end!
    count_sentence = len(sen.split('.')) - 1
    words = sen.split(' ')
    count_word = len(words)
    count_char = 0
    for word in words:
        for char in word:
            if char.isalnum():
                count_char += 1
            else:
                count_char +=1

    return count_char, count_sentence, count_word

sen = 'Hi i am ujjwal. i am 24 year old. I may need to take a leave on 3rd april.'
result_char, result_sen, result_word = sen_checker(sen)
print(f"the total words are {result_word}, the total char are {result_char} and the total sentences are {result_sen}")


# 
# Q57 [Easy]   Use strip, lstrip, rstrip, upper, lower, title, capitalize on the same string and print results.

# Q58 [Easy]   Use split, join, replace, find, count, startswith, endswith on a paragraph string.
