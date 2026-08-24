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

---------
# Q4. In Python, a string can be split on a delimiter. You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Input: this is a string   

def split_and_join(line):
    split_line = line.split(' ')
    return '-'.join(split_line)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# ---------
# Q5. Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#     Input Format

# The first line contains an integer, n , denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
    
if __name__ == '__main__':
    N = int(input())
    
lst = []
for i in range(N):
    com = input()
    command = com.split()
    if 'insert' in command[0]:
       lst.insert(int(command[1]),int(command[2])) 
       
    elif 'print' in command[0]:
        print(lst)
        
    elif 'remove' in command[0]:
        lst.remove(int(command[1]))
        
    elif 'append' in command[0]:
        lst.append(int(command[1]))
        
    elif 'sort' in command[0]:
        lst.sort()
        
    elif 'pop' in command[0]:
        lst.pop()
        
    elif 'reverse' in command[0]:
        lst.reverse()
        
