# Q1. FizzBuzz: Print numbers 1–100, but 'Fizz' for multiples of 3, 'Buzz' for 5, 'FizzBuzz' for both.
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        n = "FizzBuzz"
    elif n % 3 == 0:
        n = "Fizz"
    elif n % 5 == 0:
        n = 'Buzz'
    print(n)

# different approach same thing:
for n in range(1, 101):  
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
     

# ----------------------------------------------------------------------------------------------------------------
# Q2. Given a year, determine if it's a leap year using proper Gregorian rules.

year = int(input("enter a year to check the leap year: "))

if year % 400 == 0:
    print("it is leap year")
elif year % 100 == 0:
    print("it is not a leap year")
elif year % 4 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")

# ----------------------------------------------------------------------------------------------------------------
# Q3. Write a function that takes a string representing a date in
#      "DD/MM/YYYY" format and validates it: check valid day, month,
#      year ranges and whether the day is valid for that specific month
#      (account for leap years too). 

def year_check(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def date_checker(dmy):
    list_date = dmy.split('/')
    # since this is confirmed according to the format we can just store the date inside a variable:
    day = int(list_date[0])
    month = int(list_date[1])
    year = int(list_date[2])
    day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month not in range(1,13):
        return 'Invalid Month'
    else:
        print('Valid Month - continue')
        if year < 1:
            return 'Invalid Year'
        elif year_check(year) is False:
            print('Valid Year - checking leap or not')
            if day < 1 or day > day_list[month]: 
                return 'Invalid Date'
            else:
                print('valid date')
                return 'Valid Date'
        elif year_check(year) is True:
            if year_check(year) and month == 2:
                max_days = 29
            else:
                max_days = day_list[month]
            if day <1 or day > max_days:
                return 'Invalid date'
            else:
                return 'Valid Date'

dmy = input("Enter a year in format DD/MM/YYYY: ")
if len(dmy.split('/')) != 3:
    print(dmy)
    print('invalid date')
else:
    result_date = date_checker(dmy)
    print(result_date)


# ----------------------------------------------------------------------------------------------------------------
# Q4:  Write a function `validate_password(pwd)` that returns a list of
#      failed rules. Rules: min 8 chars, at least one uppercase, one
#      lowercase, one digit, one special character (!@#$%^&*).
#      Return empty list if all rules pass.

# here how any will work is if any of the character is upper, lower, digit or special it will return true
# and if not(if there is no uppercase) true -> false, means the command will not run

def validate_password(pwd):
    failed = []

    if len(pwd)<8:
        failed.append('Min 8 charas')
    if not any(c.isupper() for c in pwd):
        failed.append('no uppercase')
    if not any(c.islower() for c in pwd):
        failed.append('no lowercase')
    if not any(c.isdigit() for c in pwd):
        failed.append('no digit')
    if not any(c in '!@#$%^&*' for c in pwd):
        failed.append('no special char')

    if len(failed) == 0:
        return []
    else:
        return failed
result = validate_password('ocal2001')
print(f'The answer is {result}')
# ----------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------
