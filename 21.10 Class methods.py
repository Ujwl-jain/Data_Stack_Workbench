# ============================================================
#                   CLASS METHODS IN PYTHON
# ============================================================
# A class method is bound to the CLASS itself, not any instance.
# It operates on the class as a whole rather than one object.
#
# DIFFERENCE FROM REGULAR METHOD:
#   Regular method  -- first argument is self (the instance)
#   Class method    -- first argument is cls  (the class itself)
#
# @classmethod decorator tells Python:
# "pass the CLASS as first argument, not the instance"
#
# TWO MAIN USES:
#   1. Modify class variables properly
#   2. Alternative constructors (different ways to create objects)
# ============================================================


# ============================================================
#         USE 1 -- MODIFYING CLASS VARIABLE
# ============================================================
# WHY @classmethod IS NEEDED HERE:
# Without it, when you call e1.changecompany('Tesla'),
# Python passes e1 (the instance) as first argument.
# So cls.company = new becomes e1.company = 'Tesla'
# which creates an INSTANCE variable on e1 -- class unchanged.
# With @classmethod, cls = the class itself, so
# cls.company = new actually changes the CLASS variable.

# WITHOUT @classmethod -- does NOT change class variable:
class Employee:
    company = 'Apple'

    def show(self):
        print(f"name: {self.name} | company: {self.company}")

    def changecompany(cls, new):    # no decorator -- cls here is actually self
        cls.company = new           # this sets INSTANCE variable, not class

e1 = Employee()
e1.name = 'Harry'
e1.show()                   # name: Harry | company: Apple

e1.changecompany('Tesla')   # sets e1.company = 'Tesla' (instance variable)
e1.show()                   # name: Harry | company: Tesla  <- looks like it worked

print(Employee.company)     # Apple  <- class variable UNCHANGED
                            # e1 just has its own instance variable shadowing it


# WITH @classmethod -- correctly changes class variable:
class Employee:
    company = 'Apple'

    def show(self):
        print(f"name: {self.name} | company: {self.company}")

    @classmethod
    def changecompany(cls, new):    # cls = Employee (the class itself)
        cls.company = new           # changes the actual class variable

e1 = Employee()
e1.name = 'Harry'
e1.show()                   # name: Harry | company: Apple

e1.changecompany('Tesla')   # cls = Employee, so Employee.company = 'Tesla'
e1.show()                   # name: Harry | company: Tesla

print(Employee.company)     # Tesla  <- class variable actually changed this time


# ============================================================
#         USE 2 -- ALTERNATIVE CONSTRUCTOR
# ============================================================
# Normal constructor only accepts one format of input.
# Alternative constructor gives you a DIFFERENT ENTRY POINT
# to create an object -- handles different input formats
# and still ends up calling __init__ the normal way.
#
# PROBLEM without alternative constructor:
# If data comes as a string 'harry-12000', you have to
# split it manually every time before creating the object.
# Messy and repeated.

class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.sal  = sal

# manual splitting every time -- messy:
string = 'john-12000'
e2 = Employee(string.split('-')[0], string.split('-')[1])
print(e2.name)      # john
print(e2.sal)       # 12000

# what if separator changes to 'john:12000' or 'john|12000'?
# you have to find and update every split call in your code.


# WITH alternative constructor -- clean, centralized:
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.sal  = sal

    @classmethod
    def fromstr(cls, string):           # alternative constructor
        name, sal = string.split('-')   # splitting handled inside class
        return cls(name, sal)           # cls = Employee, same as Employee(name, sal)
                                        # this calls __init__ and creates the object

string = 'john-12000'
e3 = Employee.fromstr(string)   # clean one liner from outside
print(e3.name)      # john
print(e3.sal)       # 12000


# ============================================================
#         HOW ALTERNATIVE CONSTRUCTOR WORKS -- STEP BY STEP
# ============================================================
#
# Employee.fromstr('john-12000')
#
# Step 1: @classmethod passes cls = Employee automatically
#         string = 'john-12000'
#
# Step 2: inside fromstr:
#         name, sal = 'john-12000'.split('-')
#         name = 'john'
#         sal  = '12000'
#
# Step 3: return cls(name, sal)
#         cls IS Employee, so this is identical to:
#         return Employee('john', '12000')
#
# Step 4: Employee('john', '12000') calls __init__
#         self.name = 'john'
#         self.sal  = '12000'
#         object is created and returned
#
# Step 5: e3 = that newly created object
#         e3.name = 'john', e3.sal = '12000'
#
# fromstr is just a different DOOR into the class.
# The actual object is still built by __init__ at the end.


# ============================================================
#          self vs cls -- SIDE BY SIDE
# ============================================================
#
#               self                        cls
#  ──────────────────────────────────────────────────────────────
#  Represents    the instance (object)       the class itself
#  Used in       regular methods             class methods
#  Decorator     none                        @classmethod
#  Accesses      instance variables          class variables
#  Example       self.name = 'Harry'         cls.company = 'Tesla'


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. @classmethod decorator is required
#  2. First parameter is cls by convention (like self for instances)
#     but you can name it anything -- cls is just the standard
#  3. cls refers to the CLASS -- not any specific object
#  4. Use to modify class variables properly from outside
#  5. Use as alternative constructor when input format varies
#  6. Alternative constructor always ends with return cls(...)
#     which internally calls __init__ to build the object
#  7. Without @classmethod, Python passes instance as first arg
#     so you end up setting instance variable not class variable
#
# ============================================================
