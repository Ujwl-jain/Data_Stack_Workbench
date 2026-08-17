# Q35 [Medium] Sort a list of tuples by the second element, then by first element as tiebreaker.

list_tup = [(1, 3), (2, 1), (4, 1), (3, 2)]

final_list = sorted(list_tup, key=lambda x: (x[1], x[0]))
print(final_list)

# Q36 [Medium] Create a named tuple for a 'Student' with fields name, grade, score. Demonstrate usage.
from collections import namedtuple

Student  = namedtuple('Student', ['name','grade','score'])
s1 = Student('Ujjwal', 'A', 95)

print(s1.name) 
print(s1.score) 
print(type(s1))
print(s1[0])  


# Q56. Given a list of (student, subject, score) tuples, return a
#      dictionary grouping scores by student:
#      {'Alice': [85, 90], 'Bob': [78]}

'''
Requirement - 
list of tuples includes the info of students
return a sorted dictonary with their scores list 

Logic
if there is a list of scores means tuple containing same name are more than 1 

lets say raw input = [(alice, maths, 85), (matter, english, 99), (alice, sciene, 18), (matter, hindi, 99)]

we will do with functions

this list will be called with the functions name and function will return as dict

function as follows -
create an empty dict = {}
first we will process through the list using loop 
for list in raw input:

then another for loop inside the loop to access the items in tuple using indexing
inside the 2nd loop we will provide the conditons(since the struture of tuple is defined in the question) first element will always be name which is key
if tuple_item[0].isaplha() and not in empty_dict:
    empty dict[tuple_item[0]] = list(tuple[2])
else:
    empty dict.append(list(tuple[2]))

CORRECT LOGIC:

Create empty dict
Loop → unpack student, subject, score
If student NOT in dict → dict[student] = [score]
Else → dict[student].append(score)
Return dict
'''

def list_to_dict(list_studnet):
    # SINCE THE ORDER IS DEFINED WE CAN UNPACK THE TUPLE WITH ITS FIELD NAME AND DIRECTLY CREATE A SOLUTION
    result_dict = {}
    for student, subject, score in list_student:
        if student not in result_dict:
           result_dict[student] = [score]
        else:
            result_dict[student].append(score)
    return result_dict


list_student = [('alice', 'maths', 85), ('matter', 'english', 99), ('alice', 'ciene', 18), ('matter', 'hindi', 99)]
result = list_to_dict(list_student)
print(result)


# METHOD 2 — Unknown order (isinstance + lookup table)
# lets say we dont know about the order inside the list of tuple like in previous question in place of list of tuple its list of sets or tuple with unknown order, then:
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict and known subjects list
# 2. Outer loop → each tuple/set
# 3. Reset score, student, subject INSIDE outer loop, OUTSIDE inner loop!
# 4. Inner loop → each item in tuple/set
#       if int → score
#       elif not in subjects list → student (name)
#       else → subject
# 5. AFTER inner loop → check student and update dict
# 6. Return dict

def list_to_dict(list_studnet):
    # SINCE THE ORDER IS DEFINED WE CAN UNPACK THE TUPLE WITH ITS FIELD NAME AND DIRECTLY CREATE A SOLUTION
    result_dict = {}
    list_subject =  ['maths', 'english', 'science', 'hindi', 'physics']
    for tup in list_student:
        score = 0
        student = ''
        subject = ''
        for item in tup:
            if isinstance(item, int):
                score = item
            elif item not in list_subject:
                student = item
            else:
                subject = item
            
        if student not in result_dict:
            result_dict[student] = [score]
        else:
            result_dict[student].append(score)

    return result_dict


list_student = [('Ujjwal',  85,'maths'), ( 'english', 'nami',99), ('Ujjwal', 'science', 18), ('matter', 'hindi', 99)]
result = list_to_dict(list_student)
print(result)
