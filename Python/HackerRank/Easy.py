# Q1. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

def swap_case(s):
    temp = ''
    for char in s:
        if char.islower():
            temp = temp + char.upper()
        elif char.isupper():
            temp = temp + char.lower()
        else:
            temp = temp + char
    return temp

---------
# Q2. You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

---------
# Q3. The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Input:

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


# The first line contains the integer n, the number of students' records. 
# The next n lines contain the names and marks obtained by a student, each value separated by a space. 
# The final line contains query_name, the name of a student to query.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
average_marks = {} 

for n, mrk in student_marks.items():
    if n not in average_marks:
        total = 0
        for i in mrk:
             total = total + i
        avg = total/len(mrk)
        average_marks[n] = f"{avg:.2f}"
        
        
print(average_marks[query_name])
