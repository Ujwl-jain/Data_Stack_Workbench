# ------------------ Exception Handling ------------------------------

'''
process of respondoing to unwanted or unexpected events or error.

Exception handling deals with these events to avoid program or system crash, and without this process, 
exception would disrupt the noraml operation
'''

# exceptions in python :
'''
Many built in functions are there in python that are raised when your program encounters an error

when there error occurs, interprator stops the current process, and pass t to the calling process
if not handled program will crash

'''

#  Simple multiplication program with currently no error, but it can be caused in an unexpected even
#  for example: what if i put a name in input, this will cause an error. 
#  then we wil put try, catch block in the place where there are chances that code might get an unexpected errorr to counter the error at the runtime
#  in the below code lets say for loop can create an unexpected error

# a = input("enter a number:")
# print(f"Multiplication table of {a} is:")

# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# else:
#     print("end of loop")

# ----------------------------------------------------------
#  So, using try catch
# we do try catch, so that our lines of code keep getting exceuted even after getting an unexpected error, program must not hault
# it helps in debugging in later stages
a = input("enter a number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    else:
        print("end of loop")

except Exception as e:
    print(f"Invalid Input: {e}")

# if we are not using exception as e in our print, we can just use except and print anything we want 
# except:
#     print(f"Invalid Input")

print("end of code")


# Multiple execption handling in except block
try:
    num = int(input("enter a number:"))
    b =[5,6,7]
    print(b[num])

# here if we put anything other than integer this block will exceute
except ValueError:
    print("invalid integer")

# here if we put the integer but the value is more than 2 then it will thorugh index error as b only has 0 to 2 index
except IndexError:
    print("index error")



# ----------------------- Fianlly Keyword ----------------------
'''
after handling exception using try catch block we can execute a finally blok at the end of code
it will always exected regardless of the fact that error occured or not
its like a conclusion of a code, it cam be anythin like closing a file, closing DB etc
'''

try:
    lst = [1,2,3]
    i = int(input("enter the index"))
    print(lst[i])
except:
    print("an error occured")

finally:
    print("i will still exceute regardless of error or not")


# Most frequent question asked is if fianlly is still going to executed then we can jist do this why use finally

try:
    lst = [1,2,3]
    i = int(input("enter the index"))
    print(lst[i])
except:
    print("an error occured")

# this will still run regardless of error or not
print("i will still exceute regardless of error or not")

# then the biggest finally benifit is:

# def is_fun():
#     try:
#         lst = [1,2,3]
#         i = int(input("enter the index"))
#         print(lst[i])
#         return True
#     except:
#         print("an error occured")
#         return False
    
#     # here it will not executed cause after returning the value it will exit the function
#     print("i will still exceute regardless of error or not")

# x = is_fun()
# print(x)

def is_fun():
    try:
        lst = [1,2,3]
        i = int(input("enter the index"))
        print(lst[i])
        return True
    except:
        print("an error occured")
        return False
    
    # here finally will going to be still executed even if try returns the value back or except returns the value back
    finally:
        print("i will still exceute regardless of error or not")

x = is_fun()
print(x)



# --------------------- RAISE KEYWORD -----------------------------

# WE CAN USE RAISE KEYWORD TO RAISE CUSTOM ERROR BY OURSELVES
# WE NEED TO CREATE CUSTOM  EXCEPTION TO SERVE OUR PURPOSE
# IT WORKS AS NOTIFICATION WHILE DEBUGGING, 
# it can be helpfull in some cases like, debugging, or taking precautions during production work 

a = int(input("enter the value betwen 5-9: "))

if a<5 or a>9:
    raise ValueError("value should be between 5-9")


# custom error using class will be done later when i will study class
