# File handling

'''
One of the most important topic in the Programming
All methods for file handling are built in.
'''

# ------------------------ opening a file -------------------
'''
python provides open() to open a file in python, it takes two arguments:
1. name of the file,
2. mode in which file should be opened, it can be 'r' for reading, 'w' for writing, 'a' for appending
'''
# -----------------------
# MODES - 'r' - read

'''
means reading mode, will perfom the reading of a file
gives error if file does not exist, this is the default mode if no mode is passed as a parameter
'''

# throughs errora as myfile.txt does not exist but if exist it will read the file as the mode is 'r'
# f = open('myfile.txt', 'r')

f = open('file_handling.txt', 'r')

# WE CAN NOT USE 'w' to extract or read the data from the file, specific mode can perform specific task only
# 'r' can not perform write, 'w' can not perform read and same for other modes
# f = open('file_handling.txt', 'w')

# r mode is by default so this will work too
# f = open('file_handling.txt')

# no point in printing only f as it will not do anythin
# print(f)

# read() - this will actaully read the file using read fnction and store its content in text variable 
text = f.read()
print(text)

# close() - this will close the file 
f.close()
# ---------------------

# ---------------------
# MODE - WRITE - 'w'
'''
means writing in the file, will perfom mainly 2 functions if file does not exist 
1. create it and 2. write it
'''
f = open('file_handling.txt', 'w')
f.write('Hi i am using mode - w to test')
# it is important to close the file eerytime we perfom a function
f.close()

# this will automatically closed the file after performing the function
# with open('file_handling', 'w') as f:
#     f.write("hi i am testing 'with' statement with mode 'w' which close the file automatically")

'''
From the above code, important things to remember
1. f.close() is must if you are modifying any thing in the code untill and unless using with statement
2. f.write will delete the data in the existing file if any and write the current statement, 
so it is recommended to use mode - 'w' when you first create a new file, later use mode - 'a' append to add the newly data
'''
# ------------------------

# ------------------------
# MODE - APPEND - 'a'
'''
Means appending in the file, it performs 2 function mainly 1. creates a file if not exist, 2. Append it
'''
f = open('file_handling.txt', 'a')
f.write('Hi i am using mode - a to test')
# it is important to close the file eerytime we perfom a function
f.close()

# this will automatically closed the file after performing the function
# with open('file_handling', 'a') as f:
#     f.write("hi i am testing 'with' statement with mode 'a' which close the file automatically")

'''
From the above code, important things to remember
1. f.close() is must if you are modifying any thing in the code untill and unless using with statement
2. f.write() in mode 'a' will not delete the data that already exist inside the file it will append in last of the file
'''
# ------------------------

# ------------------------
# MODE - create - 'x'
'''
this creates the file and gives error if file exist
'''
# f = open('file_handling2.txt', 'x')
# f.write('Hi i am using mode - x to test')
# f.close()

# ------------------------

# ------------------------
# MODE - text - 't'
# ------------------------
'''
t mode is used to handle text files, t referes to text mode, there is a difference in r and rt, w and wt, since text mode is by default
the default mode is r open for reading text, synonym of 'rt'
'''
f = open('file_handling.txt', 'rt')
text = f.read()
print(text)
f.close()

# ------------------------
# MODE - binary - 'b'
'''
Mode - binary - b used to handles binary files like pdf, images etc, the content will be in binary mode.
'''
f = open('file_handling.txt', 'rb')
text = f.read()
print(text)
f.close()


# ------------------------ MULTIPLE METHODS IN FILE HANDLING -------------------------------

# 1. read()
# already done above

# 2.readline()
'''
this method reads a single line from the file, if we want to read multiple lines then we wwill use loop
for example:
'''

f = open('file_handling2.txt', 'r')
while True:
    line = f.readline()
    print(f"the lines reading using readline(): {line}")
    if not line:
        break

'''
above program is a simple readline program, 
since we are going to work on complex data set we can just create another example to nderstand readline()

even though txt file contain integers they are still strings so from txt if you want to do some calculaation then you ahve to convert the type
'''
f = open('file_handling2.txt', 'r')
i = 0
while True:
    line = f.readline()
    i = i+1
    if not line:
        break
    
    # string values
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    m4 = line.split(',')[3]

    # converts to int to perfom math calculation
    # m1 = int(line.split(",")[0])
    # m2 = int(line.split(",")[1])
    # m3 = int(line.split(",")[2])
    # m4 = int(line.split(",")[3])

    # since the data set is string, we need to convert to int to perform accurate mathematic function for better result, other wise result will be different.
    print(f"Marks of maths for student {i} is {m1*2}")
    print(f"Marks of sst for student {i} is {m2*2}")
    print(f"Marks of gk for student {i} is {m3*2}")
    print(f"Marks of cs for student {i} is {m4*2}")



# 3.writeline()
'''
writes a sequence of string to a file. the sequence can be any iterable object, such as list or a tuple

the \n character is used to add newline to the end of string as writeline does not do it itselves, best way to add the new line for multiple line is to use the loop
'''

f = open('file_handling3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n']
f.writelines(lines)
f.close()

# with loop - then we need to use write(), there will be no use to add writeline with loop.
f = open('file_handling3.txt', 'w')
lines = ['line 1', 'line 2', 'line 3', 'line 4']
for line in lines:
    f.write(line + '\n')
f.close()

# 4. seek()
'''

'''

# 5. tell()


# 6. truncate()
