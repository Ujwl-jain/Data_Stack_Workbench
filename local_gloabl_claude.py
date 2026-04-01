# ============================================================
#               GLOBAL AND LOCAL VARIABLES IN PYTHON
# ============================================================
# Every variable in Python has a SCOPE -- the region of the
# program where that variable is accessible.
#
# TWO MAIN SCOPES:
#   Global -- defined outside all functions, accessible everywhere
#   Local  -- defined inside a function, accessible only there
#
# Python follows the LEGB rule when looking up a variable:
#   L -- Local        (inside the current function)
#   E -- Enclosing    (any outer function, for nested functions)
#   G -- Global       (top level of the script)
#   B -- Built-in     (Python's own built-ins like print, len)
# Python searches in this order and uses the FIRST match it finds.
# ============================================================


# ============================================================
#                     GLOBAL VARIABLES
# ============================================================
# Defined OUTSIDE any function.
# Accessible from anywhere in the program -- inside or outside functions.
# Exists for the entire lifetime of the program.

x = 4               # global variable
print(x)            # 4

def number():
    # no local x exists here, so Python looks outward and finds global x
    print(f"inside function, global x = {x}")

number()            # inside function, global x = 4
print(x)            # 4  <- still accessible outside too


# ============================================================
#                     LOCAL VARIABLES
# ============================================================
# Defined INSIDE a function.
# Only accessible within that function.
# Created when the function is called, destroyed when it returns.
# If a local variable has the same name as a global, the local
# one takes priority INSIDE the function -- global stays unchanged.

x = 4               # global variable

def number():
    x = 6           # local variable -- shadows the global x inside here
    y = 1           # local variable
    print(f"inside function, local x = {x}")    # 6  <- local takes priority
    print(f"inside function, local y = {y}")    # 1

number()
print(f"outside function, global x = {x}")     # 4  <- global unchanged

# print(y)          # NameError: name 'y' is not defined
                    # y only existed inside the function and is now destroyed


# ------------------------------------------------------------
# What happens when local and global share the same name
# ------------------------------------------------------------
# Python does NOT modify the global -- it creates a separate
# local variable with the same name inside the function.
# Both exist independently.

name = "global ujjwal"

def show():
    name = "local ujjwal"       # completely separate from global name
    print(name)                 # local ujjwal

show()
print(name)                     # global ujjwal  <- unchanged


# ============================================================
#                     global KEYWORD
# ============================================================
# Used inside a function to declare that a variable refers to
# the GLOBAL version -- not a new local one.
# This allows you to READ AND MODIFY the global variable from
# inside a function.
#
# WARNING: generally not recommended as good practice.
# Modifying globals from inside functions can cause unexpected
# behaviour and makes bugs harder to track down, especially
# in large programs. Better to pass values in as arguments
# and return the result instead.

x = 4
print(f"before function call, global x = {x}")     # 4

def number():
    global x            # tells Python: x here means the global x
    x = 6               # this now modifies the global x directly
    y = 1               # y is still local
    print(f"inside function, x = {x}")             # 6
    print(f"inside function, y = {y}")             # 1

number()
print(f"after function call, global x = {x}")      # 6  <- global was changed


# ------------------------------------------------------------
# Better approach -- avoid global, use arguments and return
# ------------------------------------------------------------
# Instead of modifying a global variable, pass it in and return
# the new value. This is cleaner, safer, and easier to debug.

x = 4

def update_number(x):       # x passed in as argument
    x = 6
    return x                # new value returned, global untouched

x = update_number(x)        # global x updated only by explicit reassignment
print(x)                    # 6  <- works the same, but much cleaner


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Type          Defined         Accessible          Lifetime
#  ──────────────────────────────────────────────────────────────
#  Global        Outside func    Everywhere           Whole program
#  Local         Inside func     Only inside func     During func call
#
#  LEGB Lookup Order:
#  ──────────────────────────────────────────────────────────────
#  1. Local      -- looks here first
#  2. Enclosing  -- outer function scope (nested functions)
#  3. Global     -- top-level script scope
#  4. Built-in   -- Python's own names (print, len, range, etc.)
#
#  global keyword:
#  ──────────────────────────────────────────────────────────────
#  - Declared inside a function with: global variable_name
#  - Allows reading AND modifying the global variable
#  - Avoid using it -- pass arguments and use return instead
#
#  Common Mistakes:
#  ──────────────────────────────────────────────────────────────
#  1. Printing a local variable outside its function -> NameError
#  2. Assuming local x and global x are the same variable -- they are not
#  3. Using global keyword when passing arguments would be cleaner
#  4. Modifying a global inside a function without global keyword
#     -> UnboundLocalError (Python sees assignment and treats it as local)
#
# ============================================================