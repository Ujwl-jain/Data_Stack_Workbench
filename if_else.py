# QUESTION TO PERFORM FOR IF ELSE

list_color = ['yellow', ' red', 'blue', 'black']

if 'yellow' in list_color:
    print('present')

else:
    print('add it')


# -------------------------- short hand if-else conditons --------------------------------------
# means if else in one line
# usefull when conditions are simple and can be handle in one line
# not recommended for complex statement with multiple conditon and multiple if else
a = 330 
b = 3303

print("a") if a>b else print("=") if a==b else print("B")

# another example 
c = 9 if a>b else 0
print(c)


# another example:
value_if_true = 1
value_if_false = 2

if value_if_true > value_if_false:
    result = value_if_true
else:
    result = value_if_false
print(result)

# using 1 liner
result = value_if_true if value_if_true > value_if_false else value_if_false
print(result)