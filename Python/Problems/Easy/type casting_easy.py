# ---------------------------------------------------------------------------------------------------
# Q28 [Easy]   Write a safe int converter that returns None instead of raising ValueError.

a = 'Ujjwal'

try:
    print(int(a))

except:
    print(None)

# improved version -
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# testing it
print(safe_int('Ujjwal'))  # None ✅
print(safe_int('123'))     # 123 ✅
print(safe_int('24.5'))    # None ✅ (float string also fails int conversion)


# ---------------------------------------------------------------------------------------------------
# Q29 [Easy]   Convert a list of string numbers ['1','2','3'] to actual integers using map and int.

list_s = ['1' , '2' , '3']
list_n = []
try:
    for n in list_s:
        list_n.append(int(n))
except ValueError:
    print("Invalid list") 

print(list_n)

# using map() - need to learn this

list_s = ['1', '2', '3']

list_n = list(map(int, list_s))

print(list_n)  # [1, 2, 3] 

# Q58. Take a list of boolean values and convert them to integers (0 or 1).
#      Then compute and return the sum.
