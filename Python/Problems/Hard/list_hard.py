# -----------------------------------------------------------------------------------------------------------
# Q19 [Hard]   Generate a multiplication table (1–10) as a 2D list using nested list comprehension.

table_list = []
 
for row in range(1, 11):
    list_cal = []                        # reset inner list for each row
    for column in range(1, 11):
        mat = row * column               # calculate product
        list_cal.append(mat)             # add to current row
    table_list.append(list_cal)          # add completed row to final list
 
print(table_list)
 
# -----------------------------------------------------------------------------
# METHOD 2 — Nested List Comprehension (Same result, 1 line!)
# -----------------------------------------------------------------------------
 
list_Comp = [[row * column for column in range(1, 11)] 
             for row in range(1, 11)]
 
print(list_Comp)
 


# -------------------------------------------------------------------------------------------------------
# Q20 [Hard]   Find all prime numbers up to N using list comprehension and a helper function.

n = 10
list_prime = []

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    # is this return true outside cause it will automatically says true as call condition fails for actual prime numnber?? 
    return True
    
for i in range(n):
    if is_prime(i) == True:
        list_prime.append(i)

print(list_prime)

# using list comprehenion
prime_list = [i for i in range(10) if is_prime(i) == True ]
print(prime_list)


# Q46. Write a function that takes a list of dictionaries (each with keys
#      'name' and 'score') and returns a sorted list of names of students
#      who scored above the average score.
