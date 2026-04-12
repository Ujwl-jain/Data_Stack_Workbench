# Q23 [Medium] Check if two strings are anagrams of each other.

str1 = input("enter the first string: ")
str2 = input("enter the 2nd string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("yes this is anagram")

else:
    print("it is not anagram")


# Q24 [Medium] Find the longest word in a sentence using string methods only.

# Q25 [Medium] Count frequency of each character in a string and return as a dictionary.

# Q40. Write a function that converts a snake_case string to camelCase.
#      Example: "hello_world_python" → "helloWorldPython"

# Q41. Write a function that takes a string and returns True if all
#      brackets are balanced: (), [], {}.
#      Example: "{[()]}" → True,  "{[(])}" → False

