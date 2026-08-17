# ============================================================
#                   STATIC METHODS IN PYTHON
# ============================================================
# A static method is a method inside a class that does NOT
# depend on the class or any object.
#
# 5 KEY THINGS:
# 1. Defined using @staticmethod decorator
# 2. Does NOT use self -- no access to object or class data
# 3. Belongs to the class logically but not associated with it
# 4. Can be called using object OR class name directly
# 5. Behaves like a normal function that just lives inside a class
#    for organisational purposes
#
# WHEN TO USE:
# When you need a utility function that is related to the class
# topic but does not need any data FROM the class or object.
# ============================================================


# ============================================================
#                      THE DIFFERENCE
# ============================================================
# Regular method  -- needs self, works with object's own data
# Static method   -- no self, works only with what you pass in

class Math:
    def __init__(self, num):
        self.num = num              # object's own data

    def addtonum(self, n):          # regular method
        self.num = self.num + n     # uses self -- needs the object's data

    @staticmethod
    def add(a, b):                  # static method
        return a + b                # no self -- works only with a and b
                                    # has no idea self.num even exists


a = Math(5)
print(a.num)        # 5

a.addtonum(6)       # regular method -- self = a, uses a.num
print(a.num)        # 11  <- a.num was changed using self


# ============================================================
#              TWO WAYS TO CALL A STATIC METHOD
# ============================================================
# Unlike regular methods, static methods can be called
# WITHOUT creating an object at all.

# WAY 1 -- using class name directly (most common, preferred):
result = Math.add(1, 2)
print(result)           # 3

# WAY 2 -- using an object (works but misleading):
result = a.add(1, 2)
print(result)           # 3

# Both give the same result.
# Way 1 is preferred because it makes it clear the method
# does not depend on any object -- calling via class name
# signals "this is independent utility logic."


# ============================================================
#                      REAL WORLD ANALOGY
# ============================================================
# Think of a Math class like a calculator:
#
# Regular method = buttons that depend on what number is
#                  currently on the screen (self.num)
#
# Static method  = a standalone utility like a square root
#                  button -- you just give it a number,
#                  it gives you back an answer,
#                  it does not care what was on screen before


# ============================================================
#            STATIC vs REGULAR METHOD -- SIDE BY SIDE
# ============================================================
#
#               Regular Method          Static Method
#  ──────────────────────────────────────────────────────────────
#  Decorator     None                   @staticmethod
#  First param   self                   nothing (no self)
#  Access to     object data (self.x)   only what is passed in
#  Called via    object only            object OR class name
#  Use when      needs object's data    independent utility logic


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. @staticmethod decorator is required
#  2. No self parameter -- cannot access object or class data
#  3. Call via class name: Math.add(1,2) -- preferred
#  4. Call via object: a.add(1,2) -- works but not ideal
#  5. Use when the logic is related to the class topic
#     but does not need any data from the object
#
# ============================================================
