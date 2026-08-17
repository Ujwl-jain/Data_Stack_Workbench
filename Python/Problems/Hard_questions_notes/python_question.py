# # Q3  [Medium] Given three sides of a triangle, determine if it's equilateral, isosceles, or scalene.

ang1  = int(input("enter the side of a triangle: "))
ang2  = int(input("enter the side of a triangle: "))
ang3  = int(input("enter the side of a triangle: "))

if ang1 == ang2 == ang3:
    print("it is a equilateral triangle")
elif ang1 == ang2 or ang1 == ang3 or ang2== ang3:
    print("it is isosceles")
else:
    print("it is scalene")

# ---------------------------------------------------------------------------------------------------    
# # Q4  [Medium] Write a grading system: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).

T_grade = int(input("enter the total number of percentage of your grade: "))

if T_grade < 0 or T_grade > 100:
    print("Invalid grade! Please enter between 0 and 100")
elif T_grade >= 90:
    print("Congrats!! you got an A")
elif T_grade >= 80:
    print("Yoho!! You got B")
elif T_grade >= 70:
    print("Nice!! You got C")
elif T_grade >= 60:
    print("HMMM! You got a D")
else:
    print("Better luck next time, Its F")

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

# Q17 [Medium] Remove duplicates from a list while preserving order (no set shortcuts).

list_rem = ["mango", "mango", "potato", "ice", "water", "colddrinks", "ice"]
list_original =[]

for words in list_rem:
    if words not in list_original:
        list_original.append(words)
        
list_rem = list_original
print(list_rem)

# Q35 [Medium] Sort a list of tuples by the second element, then by first element as tiebreaker.



# Q36 [Medium] Create a named tuple for a 'Student' with fields name, grade, score. Demonstrate usage.

# Q47 [Medium] Implement binary search on a sorted list using a while loop.


# Q48 [Medium] Use enumerate and zip together to pair elements from two lists with their index.


# Q49 [Medium] Write a number guessing game loop: keep guessing until correct, count attempts

# Q23 [Medium] Check if two strings are anagrams of each other.


# Q24 [Medium] Find the longest word in a sentence using string methods only.

str1 = input("enter the first string: ")
str2 = input("enter the first string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("yes this is anagram")

else:
    print("it is not anagram")