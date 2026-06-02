# ============================================================
#                    TYPECASTING IN PYTHON
# ============================================================
# Typecasting is the conversion of one data type to another.
# Example: converting a string '5' into an integer 5.
#
# TWO TYPES:
#   1. Implicit -- done automatically by Python
#   2. Explicit -- done manually by the programmer
#
# COMMON CONVERSION FUNCTIONS:
#   int()     -- converts to integer
#   float()   -- converts to float
#   str()     -- converts to string
#   bool()    -- converts to boolean
#   list()    -- converts to list
#   tuple()   -- converts to tuple
#   set()     -- converts to set
#   dict()    -- converts to dictionary
#   ord()     -- converts character to its ASCII integer value
#   hex()     -- converts integer to hexadecimal string
#   oct()     -- converts integer to octal string
# ============================================================


# ------------------------------------------------------------
# Why typecasting matters
# ------------------------------------------------------------
# Without typecasting, operations on wrong types give wrong results.

a = '2'
b = '4'
print(a + b)            # '24'  <- string concatenation, NOT addition
print(int(a) + int(b))  # 6     <- correct, after converting to int


# ============================================================
#               TYPE 1 -- IMPLICIT TYPECASTING
# ============================================================
# Python automatically converts a lower-order type to a higher-order
# type to prevent data loss during an operation.
# No user involvement needed -- Python handles it silently.
#
# ORDER (low to high):
#   bool -> int -> float -> complex
#
# Rule: result always takes the type of the HIGHER-order operand.
# ============================================================

c = 11.9        # float  (higher order)
d = 10          # int    (lower order)
result = c + d
print(result)           # 21.9   <- result is float, not int
print(type(result))     # <class 'float'>

# bool is treated as int (True=1, False=0):
print(True + 5)         # 6      <- bool implicitly becomes int
print(True + 5.0)       # 6.0    <- bool becomes float

# Python will NOT implicitly convert between unrelated types:
# print('5' + 5)        # TypeError -- str and int cannot mix


# ============================================================
#               TYPE 2 -- EXPLICIT TYPECASTING
# ============================================================
# The programmer manually converts a value using conversion functions.
# Needed when Python cannot or will not convert automatically.
# ============================================================

string = '15'
b = 5
print(int(string) + b)          # 20  <- manually converted string to int

# str() -- convert number to string
age = 21
print("my age is " + str(age))  # 'my age is 21'
# print("my age is " + age)     # TypeError without str()

# float() -- convert int or valid string to float
print(float(10))                # 10.0
print(float('3.14'))            # 3.14

# bool() -- almost everything is True except empty/zero values
print(bool(0))                  # False
print(bool(1))                  # True
print(bool(''))                 # False  <- empty string
print(bool('hello'))            # True
print(bool([]))                 # False  <- empty list
print(bool([1, 2]))             # True

# list(), tuple(), set() -- convert between collection types
print(list((1, 2, 3)))          # [1, 2, 3]  <- tuple to list
print(tuple([1, 2, 3]))         # (1, 2, 3)  <- list to tuple
print(set([1, 2, 2, 3]))        # {1, 2, 3}  <- list to set, removes duplicates

# ord() -- character to its ASCII integer value
print(ord('A'))                 # 65
print(ord('a'))                 # 97

# hex() and oct() -- integer to hex or octal string
print(hex(255))                 # '0xff'
print(oct(8))                   # '0o10'


# ============================================================
#                     IMPORTANT RULES
# ============================================================
# 1. The value must be VALID for the target type
#    int('hello')     -> ValueError  (letters cannot become int)
#    int('15')        -> works fine  (numeric string is valid)
#    int('15.5')      -> ValueError  (use float() first, then int())
#    int(float('15.5')) -> 15        (correct two-step approach)
#
# 2. int() on a float TRUNCATES -- does NOT round
#    int(9.9)  -> 9    (not 10)
#    int(-3.7) -> -3   (not -4)
#
# 3. Converting float string directly to int will cause an error:
#    int('3.14')       -> ValueError
#    int(float('3.14'))-> 3          (convert to float first)
# ============================================================


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Function     Converts To       Notes
#  ──────────────────────────────────────────────────────────────
#  int(x)       Integer           Truncates floats, no letters
#  float(x)     Float             Works with int and numeric strings
#  str(x)       String            Works with almost anything
#  bool(x)      Boolean           0/empty = False, rest = True
#  list(x)      List              Works on any iterable
#  tuple(x)     Tuple             Works on any iterable
#  set(x)       Set               Removes duplicates
#  ord(x)       Integer (ASCII)   Single character only
#  hex(x)       Hex string        Integer input only
#  oct(x)       Octal string      Integer input only
#
#  Implicit order (low to high): bool -> int -> float -> complex
#  Result type = highest-order type in the operation
#
# ============================================================
