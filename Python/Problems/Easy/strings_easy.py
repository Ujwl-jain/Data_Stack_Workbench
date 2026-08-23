# ---------------------------------------------------------------------------------------------------
# Q1   Count vowels in a string without using any built-in count method.
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
# Q2   Reverse words in a sentence (not characters).

string_rev = 'i am ujjwal jain and i am 24 years old'
list_rev = string_rev.split()[::-1]

rev_string = ' '.join(list_rev)
print(rev_string)


# -----------------------------------------------------------------------------------------------------
# Q3. Write a function that takes a sentence and returns the number of
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
# Q4 [Easy]   Use strip, lstrip, rstrip, upper, lower, title, capitalize on the same string and print results.

# Q5 [Easy]   Use split, join, replace, find, count, startswith, endswith on a paragraph string.

# Q6. Write a function that takes a sentence and uses a lambda to
#      capitalize the first letter of every word that has more than
#      3 characters. Leave shorter words unchanged.
'''
my understanding:

takes a sentense lets say - I am ujjwal Jain, i am student of data science and c++

we will perfomr using normal function approach and lambda

basically, capitalise the word of sentence which has a len of moer than 3 like ujjwal jain, data etc etc a
and leave I, am etc unchanaged
'''
def sen_capitaliser(st):
    st_list = st.split()
    st_result = []
    for word in st_list:
        if len(word) > 3:
            r = word.capitalize()
            st_result.append(r)
        else:
            st_result.append(word)
    
    return ' '.join(st_result)

str_input = 'I am ujjwal Jain, i am student of age 24 of data science and c++'
print(f'The result after performing capitalisatio : {sen_capitaliser(str_input)}')

# using lambda - map
st_result = list(map(lambda x: x.capitalize() if len(x)>3 else x, str_input.split()))
print(' '.join(st_result))


# Q7. Import the `string` module. Write a function that removes all
#      punctuation from a given string using string.punctuation.

'''
My understanding import a function from string lib, and use it to remove al punctuation from a string
punctuation - anything that is not a number and digit, means special character

punctuation lib - in built library to filter out special character from the string or it is a list of special character

'''
from string import punctuation as pun

# using normal approcah
def punctuation_cleaner(st):
    final_str = ''
    for char in st:
        if char.isdigit() or char.isalpha() or char == ' ':
           final_str = final_str + char

    return final_str

test = "Hello, World! How are you? I'm fine... Thanks #1!"
print(f'The result after performing punctuation cleaning : {punctuation_cleaner(test)}')

# using punctuation lib

def punctuation_cleaner(st):
    final_str = ''
    for char in st:
        if char not in pun:
           final_str = final_str + char

    return final_str

test_pun = "Hello, World! How are you? I'm fine... Thanks #1!"
print(f'The result after performing punctuation cleaning : {punctuation_cleaner(test_pun)}')


# Q8. Write a function `mask_email(email)` that returns the email
#      with all characters before '@' replaced by '*' except the
#      first and last character.
#      Example: "ujjwal@gmail.com" → "u*****l@gmail.co else x"

'''
My understanding:

basically make the string * before @ except first and last letter before @\

'''

def mask_email(email):
    mask_list = email.split('@')
    username = mask_list[0]
    domain = mask_list[1]
    masked_email = ''
    for char in range(len(username)):
        if char == 0 or char == len(username) - 1:
            masked_email = masked_email + username[char]
        else:
            masked_email = masked_email + '*'
    
    return (masked_email + '@' + domain)


test_email = "jain24ujjwal24@gmail.com"
print(f'The result after masking email : {mask_email(test_email)}')


-------------------------
# Q9. Write a function that takes a sentence and uses a lambda to
#      capitalize the first letter of every word that has more than
#      3 characters. Leave shorter words unchanged.

sen = 'i am ujjwal jain, i am two zero two four born'

final = list(map(lambda x: x.capitalize() if len(x)>3 else x, sen.split()))

print(' '.join(final))
