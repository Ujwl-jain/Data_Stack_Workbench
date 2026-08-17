# =============================================================================
# Q36 [Medium] - Named Tuple
# Create a 'Student' named tuple with fields name, grade, score
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A NAMED TUPLE is like a regular tuple but with FIELD NAMES!
#
# Regular tuple — access by index only, confusing:
#   s1 = ('Ujjwal', 'A', 95)
#   s1[2]   # what is index 2 again?? 🤔
#
# Named tuple — access by name, crystal clear:
#   s1 = Student('Ujjwal', 'A', 95)
#   s1.score   # ✅ instantly readable!
#
# Think of it as CREATING YOUR OWN DATA TYPE:
#   int, str, list → built-in types
#   Student        → YOUR custom type!
#
# Just like int(5) creates an integer,
# Student('Ujjwal', 'A', 95) creates a Student!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — The two 'Student' names
# -----------------------------------------------------------------------------
# Student = namedtuple('Student', ['name', 'grade', 'score'])
#    ↑                     ↑
# Python variable      Internal type name (shows when printing)
#
# Left side  → variable you use in code to create instances
# Inside str → official name Python uses when displaying the type
#
# Best practice → keep both the same!
# They don't HAVE to match but keeping them same avoids confusion.


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — The list is just the BLUEPRINT
# -----------------------------------------------------------------------------
# ['name', 'grade', 'score'] is just field NAMES — used once to define structure!
# Think of it like a house blueprint:
#
#   ['name', 'grade', 'score']    ← blueprint (list, used once)
#   Student('Ujjwal', 'A', 95)    ← actual house built from blueprint (tuple)
#
# Blueprint used once → build as many instances as you want!
# You can also pass field names as string — both work:
#   namedtuple('Student', ['name', 'grade', 'score'])  # list ✅
#   namedtuple('Student', 'name grade score')           # string ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — It's still a tuple underneath!
# -----------------------------------------------------------------------------
# Named tuple = regular tuple + field names
# Same memory, same speed — just more readable!
#
# Both access methods work:
#   s1.name   → by field name ✅  (new feature!)
#   s1[0]     → by index     ✅  (still works like normal tuple!)
#
# Immutable like regular tuple — can't change values after creation!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — collections library
# -----------------------------------------------------------------------------
# Just like random is a library for randomness,
# collections is a library for ADVANCED DATA STRUCTURES.
# namedtuple is one tool inside it!
#
# from collections import namedtuple  ← grab only what you need


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

from collections import namedtuple

# Step 1 — Define the blueprint (create the type)
Student = namedtuple('Student', ['name', 'grade', 'score'])

# Step 2 — Create instances
s1 = Student('Ujjwal', 'A', 95)
s2 = Student('Rahul',  'B', 78)
s3 = Student('Priya',  'A', 88)

# Step 3 — Access fields
print(s1.name)    # Ujjwal  ← by field name
print(s1.grade)   # A
print(s1.score)   # 95
print(s1[0])      # Ujjwal  ← by index still works!

print(s1)         # Student(name='Ujjwal', grade='A', score=95)
print(s2)         # Student(name='Rahul', grade='B', score=78)


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. namedtuple creates a NEW data type with named fields
# 2. The list ['name','grade','score'] is just the blueprint — used once!
# 3. Both .fieldname and [index] access work
# 4. Two 'Student' names — variable name and internal type name — keep them same!
# 5. from collections import namedtuple — grab only what you need
# 6. Immutable like regular tuple — can't change values after creation!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER
# -----------------------------------------------------------------------------
# from collections import namedtuple
#
# TypeName = namedtuple('TypeName', ['field1', 'field2', 'field3'])
# instance = TypeName(value1, value2, value3)
#
# instance.field1   ← access by name
# instance[0]       ← access by index
#
# Use when:
#   - Tuple data has clear meaning (coordinates, student records, RGB colors)
#   - You want readability without full class overhead
#   - Data shouldn't change after creation (immutable)
