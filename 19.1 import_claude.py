# ============================================================
#                  IMPORTING IN PYTHON
# ============================================================
# Importing is the process of loading code from a Python module
# into your current file so you can use its functions, classes,
# and variables without rewriting them yourself.
#
# THREE THINGS YOU CAN IMPORT FROM:
#   1. Built-in modules  -- come with Python (math, os, random, etc.)
#   2. Third-party       -- installed via pip (pandas, numpy, etc.)
#   3. Custom modules    -- your own .py files
#
# SYNTAX OPTIONS:
#   import module                      -- import the whole module
#   from module import function        -- import specific item
#   from module import *               -- import everything (avoid)
#   import module as alias             -- import with a short name
#   from module import function as f   -- import item with alias
# ============================================================


# ============================================================
#               METHOD 1 -- import module
# ============================================================
# Imports the entire module.
# You must use the module name as a prefix every time you call
# one of its functions -- module.function_name()

import math

print(math.floor(4.4352))      # 4     <- rounds DOWN
print(math.ceil(4.4352))       # 5     <- rounds UP
print(math.sqrt(9))            # 3.0   <- square root
print(math.pi)                 # 3.141592653589793
print(math.pow(2, 8))          # 256.0 <- 2 to the power 8

# full syntax pattern:
# import module_name
# module_name.function_name()


# ============================================================
#               METHOD 2 -- from module import function
# ============================================================
# Imports only SPECIFIC functions or variables from a module.
# No need to use the module name as a prefix after this.
# Cleaner when you only need a few things from a large module.

from math import sqrt, pi

result = sqrt(9) * pi
print(result)           # 9.42477796076938

# can also import constants directly:
from math import e
print(e)                # 2.718281828459045  <- Euler's number


# ------------------------------------------------------------
# from module import * -- import everything
# ------------------------------------------------------------
# Imports ALL functions and variables from a module.
# NOT recommended because:
#   - You don't know what names are being brought in
#   - Can accidentally overwrite your own variables with same names
#   - Makes code harder to read and debug

# from math import *    # avoid unless you know exactly what you are doing


# ============================================================
#               METHOD 3 -- import as (alias)
# ============================================================
# Gives the module or function a shorter nickname (alias).
# Useful in large programs where you type the module name many times.
# Convention: use short but meaningful aliases (pd, np, m, etc.)

import math as m

result = m.sqrt(9)
print(result)           # 3.0  <- using alias instead of full name

# common real-world aliases you will see everywhere:
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import tensorflow as tf


# aliasing specific imported functions:
from math import sqrt as s, pi

result = s(9) * pi
print(result)           # 9.42477796076938


# ============================================================
#                    dir() FUNCTION
# ============================================================
# Returns a LIST of all functions, classes, and variables
# available inside a module.
# Useful when you are exploring a new module and don't know
# what tools it offers.

import math

print(dir(math))
# Output: ['__doc__', '__loader__', ..., 'ceil', 'floor',
#          'log', 'pi', 'pow', 'sqrt', 'tan', ...]

# checking a specific attribute from the module:
print(math.nan)             # nan  <- not a number constant
print(type(math.nan))       # <class 'float'>

# dir() works on anything -- not just modules:
print(dir([]))              # shows all list methods
print(dir(""))              # shows all string methods


# ============================================================
#                    CUSTOM MODULES
# ============================================================
# You can import from your OWN .py files exactly the same way
# as built-in or third-party modules.
#
# HOW IT WORKS:
#   1. You have a file called recursion.py in the same folder
#   2. Inside it, there is a function called factorial()
#   3. You import it here and use it as if you wrote it here
#
# WHY USE CUSTOM MODULES:
#   - Keeps your code organized across multiple files
#   - Increases reusability -- write once, import anywhere
#   - Easier to maintain -- update one file, changes reflect everywhere

from recursion import factorial

result = factorial(5)
print(result)           # 120

# with alias:
# from recursion import factorial as f
# result = f(5)
# print(result)         # 120


# ============================================================
#               COMMONLY USED BUILT-IN MODULES
# ============================================================
# These come with Python -- no installation needed.
#
#   math        -- mathematical functions (sqrt, floor, ceil, pi)
#   random      -- generate random numbers and choices
#   os          -- interact with the operating system (files, paths)
#   sys         -- system-specific functions and variables
#   datetime    -- work with dates and times
#   time        -- time-related functions, sleep()
#   string      -- string constants and helper utilities
#   json        -- read and write JSON data
#   re          -- regular expressions for pattern matching
#
# Quick examples:

import random
print(random.randint(1, 10))        # random integer between 1 and 10
print(random.choice(['a', 'b', 'c']))  # random item from a list

import os
print(os.getcwd())                  # prints current working directory

import datetime
print(datetime.date.today())        # prints today's date


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Syntax                            When to Use
#  ──────────────────────────────────────────────────────────────
#  import module                     Need many things from a module
#  from module import func           Need only specific items
#  from module import *              Avoid -- pollutes namespace
#  import module as alias            Long module name used often
#  from module import func as alias  Rename to avoid conflicts
#  dir(module)                       Explore what a module contains
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Imports go at the TOP of the file -- standard convention
#  2. Built-in modules first, then third-party, then custom
#  3. Use aliases that are short but still meaningful
#  4. Avoid 'from module import *' in production code
#  5. Custom module file must be in the SAME folder (or added to path)
#
# ============================================================
