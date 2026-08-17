# =============================================================================
# Q38 [Hard] - Date Validator
# Validate a date string in "DD/MM/YYYY" format including leap years
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Take a date string like "29/02/2024" and check if it's a REAL valid date.
#
# What makes a date VALID?
#   "31/01/2024" → valid   ✅  January has 31 days
#   "29/02/2024" → valid   ✅  2024 is a leap year!
#   "29/02/2023" → invalid ❌  2023 is NOT a leap year
#   "31/04/2024" → invalid ❌  April only has 30 days
#   "15/13/2024" → invalid ❌  month 13 doesn't exist!
#   "00/01/2024" → invalid ❌  day 0 doesn't exist!
#
# LEAP YEAR RULES (Gregorian calendar):
#   divisible by 4   → possible leap year
#   divisible by 100 → NOT a leap year (exception!)
#   divisible by 400 → IS a leap year  (exception to exception!)
#
#   2024 → div by 4, not 100 → leap year   ✅
#   1900 → div by 100, not 400 → NOT leap  ❌
#   2000 → div by 400 → leap year          ✅


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# HELPER FUNCTION year_check(year):
#   1. If year % 400 == 0 → True (leap year)
#   2. elif year % 100 == 0 → False (not leap)
#   3. elif year % 4 == 0 → True (leap year)
#   4. else → False
#
# MAIN FUNCTION date_checker(dmy):
#   1. Split by '/' → get list of 3 parts
#   2. Convert day, month, year to integers using indexing
#   3. Define days_in_month list (index 0 unused, index 1=Jan ... 12=Dec)
#   4. Check month in range 1–12
#   5. Check year >= 1
#   6. Determine max_days:
#      → if leap year AND month == 2 → max_days = 29
#      → else → max_days = day_list[month]
#   7. Check day between 1 and max_days
#   8. Return Valid or Invalid message
#
# FORMAT CHECK (before calling function):
#   Check len(dmy.split('/')) == 3


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — days_in_month list (index trick)
# -----------------------------------------------------------------------------
# Store max days per month in a list where INDEX = MONTH NUMBER:
#
#   day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#               ↑   ↑   ↑   ↑
#            index0 Jan Feb Mar ...
#
# Index 0 is unused (no month 0) — makes indexing natural!
# day_list[1] = 31  → January has 31 days
# day_list[2] = 28  → February has 28 days (non-leap)
# day_list[4] = 30  → April has 30 days


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Leap year affects ONLY February
# -----------------------------------------------------------------------------
# When it IS a leap year, only February changes (28 → 29)
# Other months stay the same!
#
# ❌ WRONG condition:
#   year_check(year) is True or month == 2
#   → triggers for ANY month in leap year OR Feb in non-leap year!
#
# ✅ CORRECT — BOTH conditions must be true:
#   if year_check(year) and month == 2:
#       max_days = 29        # only February in a leap year!
#   else:
#       max_days = day_list[month]
#
# max_days is just a plain integer — no list indexing needed after!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Indentation controls which block owns a line
# -----------------------------------------------------------------------------
# ❌ WRONG — day check INSIDE else, February never checked!
#   if year_check(year) and month == 2:
#       max_days = 29
#       # dead end! no check for February!
#   else:
#       max_days = day_list[month]
#       if day < 1 or day > max_days:   # only runs for non-February!
#           return 'Invalid Date'
#
# ✅ CORRECT — day check OUTSIDE, both paths merge into same checkpoint:
#   if year_check(year) and month == 2:
#       max_days = 29          # February on-ramp
#   else:
#       max_days = day_list[month]  # Other months on-ramp
#                                   # ← both roads meet here!
#   if day < 1 or day > max_days:   # runs for ALL months ✅
#       return 'Invalid Date'
#
# Think of it like two on-ramps merging onto one highway — every month
# goes through the SAME day check regardless! 🎯


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — Format check uses len() not direct comparison
# -----------------------------------------------------------------------------
# ❌ WRONG — comparing list to integer!
#   if dmy.split('/') != 3
#
# ✅ CORRECT — check the LENGTH of the list:
#   if len(dmy.split('/')) != 3


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 5 — and vs or in range checks
# -----------------------------------------------------------------------------
# A number can't be less than 1 AND greater than 31 at the same time!
#
# ❌ WRONG — condition NEVER triggers!
#   if day < 1 and day > day_list[month]
#
# ✅ CORRECT — invalid if EITHER condition is true:
#   if day < 1 or day > max_days


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

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
    day   = int(list_date[0])        # DD
    month = int(list_date[1])        # MM
    year  = int(list_date[2])        # YYYY

    day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #            ↑ index 0 unused → index 1=Jan, 2=Feb ... 12=Dec

    if month not in range(1, 13):
        return 'Invalid Month'

    if year < 1:
        return 'Invalid Year'

    # determine max days for this month
    if year_check(year) and month == 2:  # leap year AND February?
        max_days = 29
    else:
        max_days = day_list[month]

    if day < 1 or day > max_days:        # day check for ALL months
        return 'Invalid Date'
    else:
        return 'Valid Date'


dmy = input("Enter a date in format DD/MM/YYYY: ")
if len(dmy.split('/')) != 3:             # format check first!
    print('Invalid format')
else:
    result_date = date_checker(dmy)
    print(result_date)


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Test Cases
# -----------------------------------------------------------------------------
#
#  Input: "29/02/2024"
#  ┌─────────────────────────────────────────────────────────┐
#  │ list_date = ['29', '02', '2024']                        │
#  │ day=29, month=2, year=2024                              │
#  │ month in range(1,13)?  2 ✅                             │
#  │ year >= 1?             2024 ✅                          │
#  │ year_check(2024)?      2024%4=0, not %100 → True        │
#  │ leap AND month==2?     True AND True → max_days = 29    │
#  │ day < 1 or day > 29?   29 > 29? No → Valid Date ✅      │
#  └─────────────────────────────────────────────────────────┘
#
#  Input: "29/02/2023"
#  ┌─────────────────────────────────────────────────────────┐
#  │ day=29, month=2, year=2023                              │
#  │ year_check(2023)?  2023%4≠0 → False                     │
#  │ leap AND month==2? False → max_days = day_list[2] = 28  │
#  │ day < 1 or day > 28?  29 > 28? Yes → Invalid Date ❌    │
#  └─────────────────────────────────────────────────────────┘
#
#  Input: "31/04/2024"
#  ┌─────────────────────────────────────────────────────────┐
#  │ day=31, month=4, year=2024                              │
#  │ max_days = day_list[4] = 30  (April has 30 days)        │
#  │ day < 1 or day > 30?  31 > 30? Yes → Invalid Date ❌    │
#  └─────────────────────────────────────────────────────────┘
#
#  Input: "15/13/2024"
#  ┌─────────────────────────────────────────────────────────┐
#  │ month=13                                                │
#  │ 13 in range(1,13)? No → Invalid Month ❌                │
#  └─────────────────────────────────────────────────────────┘


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. days_in_month list — index 0 unused so index = month number directly!
# 2. Leap year affects ONLY February — use AND not OR in condition
# 3. Indentation = ownership — outside means ALL paths go through it
# 4. max_days is just an integer — set it once, use it cleanly
# 5. Format check uses len() — can't compare list to integer directly
# 6. day < 1 OR day > max_days — invalid if EITHER extreme is hit
# 7. Two helper functions keep code clean and readable


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Validation Function Pattern
# -----------------------------------------------------------------------------
# Whenever you need to validate input with multiple rules:
#
#   def validate(input):
#       # 1. format check first
#       # 2. check each component range (month, year)
#       # 3. handle special cases (leap year, days per month)
#       # 4. final range check using computed max value
#       # 5. return clear True/False or message
#
# Validation order matters — check format BEFORE content,
# check ranges BEFORE special cases!
#
# This pattern appears in:
#   - Date validation
#   - Email/phone number validation
#   - Password strength checker
#   - Form input validation
#   - Any "is this input correct?" problem
