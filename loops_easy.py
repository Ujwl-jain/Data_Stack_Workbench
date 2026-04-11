
#  Print the following pattern using loops:
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5

for row in range(1,6):
    for i in range(1,row+1):
        print(i, end = ' ')
    print()

# -------------------------------------------------------------------------------------------------
#  Print a pattern: right-angled triangle of stars with n rows using nested loops.

# -------------------------------------------------------------------------------------------------
#  Find the sum of all digits of a number using a while loop.

# using for loop - wrong code according to the question, correct working
list1 = [5,1,40,20,199,4,19,77]
sum = 0
sum1 = 0
for n in list1:
    sum = sum + n

print(f'the sum of all the numbers in list is: {sum}')

# using while loop actual code of that question
num = int(input("enter a more than 3 digit number: "))
total = 0
while num>0:
    digit = num%10
    total = total + digit
    num = num // 10

print(total)