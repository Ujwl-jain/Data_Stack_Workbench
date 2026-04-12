# =============================================================================
# Q26 [Hard] - Caesar Cipher
# Shift each letter by k positions, preserve case and non-letters
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A Caesar cipher is one of the oldest encryption techniques.
#
# Rules:
#   - Shift every LETTER forward by k positions in the alphabet
#   - If k = 3 → A becomes D, B becomes E, Z wraps around to C
#   - UPPERCASE stays uppercase, LOWERCASE stays lowercase
#   - Non-letters (spaces, punctuation, digits) are LEFT UNTOUCHED
#
# Example:
#   Input  : "Hello, World!"   k = 3
#   Output : "Khoor, Zruog!"


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Take the input string and value k
# 2. Create an empty result string
# 3. Loop through each character in the string
# 4. If the character is LOWERCASE → shift using 'a' as base
# 5. If the character is UPPERCASE → shift using 'A' as base
# 6. If it's anything else (space, digit, punctuation) → keep as-is
# 7. Add the processed character to the result string
# 8. Print the final result


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — How Shifting Works (ord + chr + % 26)
# -----------------------------------------------------------------------------
# Python gives us two tools:
#   ord(char)   → converts character to ASCII number  e.g. ord('A') = 65
#   chr(number) → converts ASCII number to character  e.g. chr(68)  = 'D'
#
# SHIFT FORMULA (3 steps):
#   Step 1 → Normalize to 0–25:  ord(char) - ord('A')
#   Step 2 → Add shift + wrap:   (normalized + k) % 26
#   Step 3 → Convert back:       result + ord('A')
#
# For UPPERCASE:  chr((ord(char) - ord('A') + k) % 26 + ord('A'))
# For LOWERCASE:  chr((ord(char) - ord('a') + k) % 26 + ord('a'))
#
# WHY % 26?
#   The alphabet has 26 letters. % 26 keeps the result within 0–25.
#   Example: 'Y' shifted by 3
#     ord('Y') - ord('A') = 24
#     (24 + 3) % 26       = 1    ← wraps around!
#     1 + ord('A')        = 66
#     chr(66)             = 'B'  ✅


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

str_CC = 'Hello! World$!'
k = 3
str_c = ''

for char in str_CC:
    if char.islower():
        char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    elif char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    # else: non-letters stay unchanged (space, !, $, digits, etc.)

    str_c = str_c + char

print(str_c)
# Output: Khoor! Zruog$!


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Step by Step  |  Input: 'Hello! World$!'  |  k = 3
# -----------------------------------------------------------------------------
#
#  str_c starts as ''
#
#  Step  | char | Condition   | Calculation                        | Result | str_c
#  ------+------+-------------+------------------------------------+--------+----------------
#    1   |  H   | isupper()   | (72-65+3)%26+65 = 10%26+65 = 75   |  K     | 'K'
#    2   |  e   | islower()   | (101-97+3)%26+97 = 7%26+97 = 104  |  h     | 'Kh'
#    3   |  l   | islower()   | (108-97+3)%26+97 = 14%26+97 = 111 |  o     | 'Kho'
#    4   |  l   | islower()   | same as above                      |  o     | 'Khoo'
#    5   |  o   | islower()   | (111-97+3)%26+97 = 17%26+97 = 114 |  r     | 'Khoor'
#    6   |  !   | else        | unchanged                          |  !     | 'Khoor!'
#    7   |  ' ' | else        | unchanged                          |  ' '   | 'Khoor! '
#    8   |  W   | isupper()   | (87-65+3)%26+65 = 25%26+65 = 90   |  Z     | 'Khoor! Z'
#    9   |  o   | islower()   | (111-97+3)%26+97 = 17%26+97 = 114 |  r     | 'Khoor! Zr'
#   10   |  r   | islower()   | (114-97+3)%26+97 = 20%26+97 = 117 |  u     | 'Khoor! Zru'
#   11   |  l   | islower()   | same as step 3                     |  o     | 'Khoor! Zruo'
#   12   |  d   | islower()   | (100-97+3)%26+97 = 6%26+97 = 103  |  g     | 'Khoor! Zruog'
#   13   |  $   | else        | unchanged                          |  $     | 'Khoor! Zruog$'
#   14   |  !   | else        | unchanged                          |  !     | 'Khoor! Zruog$!'
#
#  ✅ Final Output: 'Khoor! Zruog$!'


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. islower() and isupper() already imply isalpha() — no need to check both!
# 2. Always call methods with ()  →  char.isalpha()  NOT  char.isalpha
# 3. % 26 is the wrap-around trick for any circular sequence of 26 items
# 4. ord() and chr() are your best friends for character manipulation
# 5. Build result string by concatenating inside the loop


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER
# -----------------------------------------------------------------------------
# Whenever you need to "shift within a fixed range":
#   new_value = (current_position + shift) % range_size
#
# This pattern appears in:
#   - Caesar cipher (letters, range = 26)
#   - Circular arrays / queues
#   - Clock arithmetic (hours, range = 12 or 24)
#   - Day of week calculations (range = 7)
