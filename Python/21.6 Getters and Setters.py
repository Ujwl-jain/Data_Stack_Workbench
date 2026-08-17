# ============================================================
#                 GETTERS AND SETTERS IN PYTHON
# ============================================================
# Used to CONTROL how private attributes are read and changed
# from OUTSIDE the class.
#
# WHY THEY EXIST:
# When you mark an attribute as private with _ like self._value,
# the intention is "don't access this directly from outside."
# But Python does not enforce this -- nothing stops obj._value = 99.
#
# Getters and setters give you a proper controlled way to:
#   GETTER -- controlled READ  of a private value (@property)
#   SETTER -- controlled WRITE of a private value (@property_name.setter)
#
# WHERE THE VALUE ACTUALLY LIVES:
#   self._value is the single source of truth.
#   Getter reads from it.
#   Setter writes to it.
#   Regular methods also read and write to it from inside the class.
#   They never talk to each other -- all three work on self._value directly.
# ============================================================


# ============================================================
#                         GETTER
# ============================================================
# @property turns a method into a readable attribute.
# From outside the class it looks like you are reading a variable
# but you are actually running a method behind the scenes.
#
# WITHOUT @property:
#   obj._value  <- works but accesses private directly, not ideal
#   obj.value   <- AttributeError, 'value' does not exist
#
# WITH @property:
#   obj.value   <- looks like attribute, runs getter method silently

class BankAccount:
    def __init__(self, balance):
        self._balance = balance     # private attribute

    @property
    def balance(self):              # GETTER
        return self._balance        # reads and returns self._balance

account = BankAccount(1000)

print(account._balance)     # 1000 <- direct access, works but not ideal
print(account.balance)      # 1000 <- getter runs, returns self._balance
                            # no parentheses -- looks like attribute not method


# ============================================================
#                         SETTER
# ============================================================
# @property_name.setter controls HOW a private value is CHANGED
# from outside the class.
# Triggered ONLY when you assign: obj.balance = something
# Its job is to act as a GATEKEEPER -- validate or transform
# the value before storing it into self._balance.
#
# RULE: setter method name MUST match the @property name exactly.
#
# TWO ENTRY POINTS FOR CHANGING self._balance:
#   From OUTSIDE -- obj.balance = x    -> setter runs (gatekeeper)
#   From INSIDE  -- self._balance = x  -> direct, no gatekeeper needed
#                   regular methods are trusted, they are part of the class

class BankAccount:
    def __init__(self, balance):
        self._balance = balance     # __init__ sets directly, bypasses setter

    @property
    def balance(self):              # GETTER -- triggered on READ
        return self._balance

    @balance.setter
    def balance(self, amount):      # SETTER -- triggered on WRITE from outside
        if amount < 0:
            print("Cannot set negative balance -- rejected")
        else:
            self._balance = amount  # stores only if valid

    def buy_something(self, price):     # regular method -- works INSIDE class
        if price > self._balance:       # reads self._balance directly
            print("Insufficient funds")
        else:
            self._balance -= price      # writes self._balance directly
            print(f"Purchase successful. Remaining balance: {self._balance}")


account = BankAccount(1000)
print(account.balance)          # 1000

# setter triggered -- change coming from OUTSIDE:
account.balance = 500           # valid -- setter stores 500
print(account.balance)          # 500

account.balance = -100          # invalid -- setter rejects, value unchanged
print(account.balance)          # 500  <- still 500

# regular method -- change happening INSIDE the class:
account.buy_something(200)      # Purchase successful. Remaining balance: 300
print(account.balance)          # 300  <- getter reads current self._balance

account.buy_something(400)      # 400 > 300 -- Insufficient funds
print(account.balance)          # 300  <- unchanged


# ============================================================
#              GETTER vs SETTER vs REGULAR METHOD
# ============================================================
#
# Think of it like a bank building:
#
#   Setter         = front door with security check
#                  = someone from OUTSIDE trying to change balance
#                  = validates before allowing entry
#
#   Regular method = bank employee working inside the building
#                  = already inside, trusted
#                  = can touch self._balance directly, no check needed
#
#   Getter         = the window where you check your balance
#                  = controlled READ, no modification
#
#
#  Who triggers what:
#  ──────────────────────────────────────────────────────────────
#  account.balance = 500       OUTSIDE -- setter runs (gatekeeper)
#  account.buy_something(200)  INSIDE  -- regular method, direct access
#  print(account.balance)      READ    -- getter runs


# ============================================================
#                 HOW THE FLOW WORKS
# ============================================================
#
# self._balance is the single source of truth.
# Getter, setter, and methods all work on the SAME self._balance.
# Whatever self._balance currently holds is what everyone sees.
#
# account = BankAccount(1000)   __init__ stores self._balance = 1000
#                               setter does NOT run here -- bypassed
#
# account.balance = 500         setter runs
#                               amount = 500, valid
#                               self._balance = 500
#
# account.buy_something(200)    regular method runs
#                               reads self._balance (500)
#                               500 - 200 = 300
#                               self._balance = 300
#
# print(account.balance)        getter runs
#                               returns self._balance which is 300
#
# Setter and getter never talk to each other directly.
# self._balance is where the value lives -- they both just
# read from or write to that same place.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Term                    Meaning
#  ──────────────────────────────────────────────────────────────
#  self._balance           Private attribute -- actual storage
#  @property               Turns method into readable attribute (getter)
#  @balance.setter         Turns method into writable attribute (setter)
#  Getter                  Controls HOW value is READ from outside
#  Setter                  Controls HOW value is CHANGED from outside
#  Regular method          Works inside class -- direct access, no gate
#
#  Triggered by:
#  ──────────────────────────────────────────────────────────────
#  print(obj.balance)      getter runs   -- READ
#  obj.balance = 500       setter runs   -- WRITE from outside
#  obj.buy_something(200)  method runs   -- WRITE from inside
#  obj = MyClass(10)       __init__ runs -- bypasses setter completely
#
#  Structure:
#  ──────────────────────────────────────────────────────────────
#  @property
#  def balance(self):          getter -- name becomes the property name
#      return self._balance
#
#  @balance.setter
#  def balance(self, amount):  setter -- name MUST match getter name
#      self._balance = amount
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Setter name MUST match getter name exactly
#  2. Getter must exist before setter -- @balance.setter needs @property first
#  3. Call getter with obj.balance -- no parentheses, not obj.balance()
#  4. Call setter with obj.balance = x -- not obj.balance(x)
#  5. __init__ bypasses setter -- sets self._balance directly
#  6. Regular methods inside class can touch self._balance directly
#  7. Setter is gatekeeper for changes coming from OUTSIDE only
#
# ============================================================
