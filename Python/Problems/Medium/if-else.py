# ---------------------------------------------------------------------------------------------------
# Q1. Given three sides of a triangle, determine if it's equilateral, isosceles, or scalene.

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
# Q2. Write a grading system: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).

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

# ------------------------------------------------------------------------------------------------------------------------
# Q3. Given a list of numbers, classify each as 'small' (< 10),'medium' (10–99), or 'large' (100+). Return a list of labels.

list_n = [2,56,10,100,13,566,12,99,34,60,7]
labels = []
for n in list_n:
    if n < 10:
        labels.append('Small')
    elif n < 100:
        labels.append('Medium')
    elif n >= 100:
        labels.append('Large')
    else:
        labels.append("Invalid Integer")
    
print(f'{list_n} : {labels}')

# ------------------------------------------------------------------------------------------------------------------------
# Q4. Write a function that takes age and returns the life stage:
#      'baby' (0-2), 'child' (3-12), 'teen' (13-17),
#      'adult' (18-64), 'senior' (65+). Done

def age_checker(age):
    if age >= 3 and age <= 12:
        return f'You are still a child as your age is {age}'
    elif age >=13 and age<=17:
        return f"You are a teen as your age is {age}"
    elif age>=18 and age<=64:
        return f"Your are an adult, as your age is {age}"
    elif age>=65:
        return f"You are a senior citizen, as your age is {age}"
    else:
        return f"Awwwww!! How cute, you just born 'baby' "

age = float(input("Enter the age: "))
age_result = age_checker(age)
print(age_result)

# enhanced version:

def age_checker(age):
    if age < 0:
        return "Invalid age!"
    elif age <= 2:
        return f"Awww!! How cute, you're just a baby at {age}!"
    elif age <= 12:
        return f"You are still a child, age {age}"
    elif age <= 17:
        return f"You are a teen, age {age}"
    elif age <= 64:
        return f"You are an adult, age {age}"
    else:
        return f"You are a senior citizen, age {age}"

age = float(input("Enter the age: "))
print(age_checker(age))

# ------------------------------------------------------------------------------------------------------------------------
# Q5. Write a function `bmi_category(weight_kg, height_m)` that
#      calculates BMI and returns the category:
#      Underweight (< 18.5), Normal (18.5–24.9),
#      Overweight (25–29.9), Obese (30+).
#      Use a local variable to store the computed BMI.

def bmi_category(w, h):
    bmi = w / (h**2)
    if bmi < 18.5:
        return 'Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        return 'Normal'
    elif bmi >= 25 and bmi <= 29.9:
        return 'Overweight'
    else:
        return 'Obese'

height_m = 1.6
weight_in_kg = 56.32

if height_m < 3:
    result1 = bmi_category(weight_in_kg, height_m)
else:
   result1 = 'Invalid height, actual height should be in meters, centimerters and int not allowed'
print(f'The answer is {result1}')


# ------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
