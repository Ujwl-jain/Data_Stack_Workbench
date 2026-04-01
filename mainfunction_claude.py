# ============================================================
#                  if __name__ == '__main__'
# ============================================================
# Every Python file has a built-in variable called __name__.
# Python automatically sets its value depending on HOW the file
# is being run:
#
#   Running the file DIRECTLY   -> __name__ is set to '__main__'
#   Importing it into another   -> __name__ is set to the FILE NAME
#
# This lets you control which code runs and which does not,
# depending on whether the file is being run on its own or
# being used as a module by someone else.
# ============================================================


# ============================================================
#                   WHY YOU NEED IT
# ============================================================
# Without if __name__ == '__main__':
#
#   Suppose you have factorial.py with a function AND a print
#   statement at the bottom to test it.
#
#   When someone imports your factorial function into their code,
#   that test print at the bottom ALSO runs -- which they did not
#   ask for and did not expect. This causes confusion in complex
#   programs.
#
# With if __name__ == '__main__':
#
#   You wrap your test code inside this block.
#   Now when someone imports your file, ONLY the function is loaded.
#   The test code is blocked from running automatically.
# ============================================================


# ============================================================
#                   HOW __name__ WORKS
# ============================================================

# print(__name__)
# If you run this file directly    -> prints: __main__
# If this file is imported         -> prints: the filename (e.g. factorial)


# ============================================================
#              EXAMPLE -- WITHOUT if __name__
# ============================================================
# Suppose this is the content of factorial.py:
#
#   def factorial(n):
#       if n == 0 or n == 1:
#           return 1
#       return n * factorial(n - 1)
#
#   result = factorial(6)       # this line runs ALWAYS
#   print(result)               # even when someone just imports factorial()
#
# Problem: when another file does 'from factorial import factorial',
# Python executes the entire file top to bottom -- so factorial(6)
# and the print run uninvited in the importing file. Not ideal.


# ============================================================
#              EXAMPLE -- WITH if __name__
# ============================================================
# This is the correct version of factorial.py:
#
#   def factorial(n):
#       if n == 0 or n == 1:
#           return 1
#       return n * factorial(n - 1)
#
#   print(__name__)             # shows where the code is running from
#
#   if __name__ == '__main__':  # this block ONLY runs when file is run directly
#       result = factorial(6)
#       print(result)           # 720
#
# Now when another file imports factorial, the function loads cleanly.
# The test code inside if __name__ == '__main__' is completely ignored.


# ============================================================
#              IMPORTING FROM A GUARDED MODULE
# ============================================================
# This is your main file importing from factorial.py (or main_function2.py).
# Only the factorial function is loaded -- nothing else runs.

from mainfunction2 import factorial as f

result = f(5)
print(result)               # 120  <- clean, no side effects from the other file


# ============================================================
#                   WHAT HAPPENS STEP BY STEP
# ============================================================
#
#  SCENARIO 1 -- Running factorial.py directly:
#
#   Python sets __name__ = '__main__'
#   Function definition loads
#   print(__name__)  prints '__main__'
#   if __name__ == '__main__' is TRUE
#   factorial(6) runs and prints 720
#
#  SCENARIO 2 -- Importing factorial.py into another file:
#
#   Python sets __name__ = 'factorial'  (the filename)
#   Function definition loads  <- this is all the importer gets
#   print(__name__)  prints 'factorial'
#   if __name__ == '__main__' is FALSE
#   factorial(6) and print(720) are SKIPPED completely


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Variable / Block               Meaning
#  ──────────────────────────────────────────────────────────────
#  __name__                       Built-in variable Python sets automatically
#  __name__ == '__main__'         True only when file is run directly
#  __name__ == 'filename'         True when file is imported elsewhere
#  if __name__ == '__main__':     Guard block -- runs only on direct execution
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Always wrap test/demo code inside if __name__ == '__main__'
#  2. Function and class DEFINITIONS outside the block are always loaded
#  3. Code OUTSIDE the block but not in a function runs on import too
#  4. This pattern is standard in every professional Python project
#  5. It has two underscores on EACH side -- __name__ not _name_
#
# ============================================================