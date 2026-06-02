# ============================================================
#                    FILE HANDLING IN PYTHON
# ============================================================
# File handling allows your program to interact with files on
# your computer -- reading data from them, writing data into
# them, and managing them.
#
# All file handling methods are built into Python -- no imports needed.
#
# THE CORE FUNCTION:
#   open(filename, mode)
#   - filename : name or path of the file as a string
#   - mode     : how you want to open the file (read, write, etc.)
#
# TWO WAYS TO OPEN A FILE:
#   1. Manual   -- f = open()  then  f.close()  at the end
#   2. with     -- with open() as f:  closes automatically
#
# RECOMMENDED: always use 'with' -- it closes the file even if
# an error occurs mid-way, preventing data loss or corruption.
# ============================================================


# ============================================================
#                        FILE MODES
# ============================================================
#
#  Mode    Full Name       What it does
#  ──────────────────────────────────────────────────────────
#  'r'     read            Read only. Error if file not found.
#  'w'     write           Write only. Creates file if not found.
#                          DELETES existing content and rewrites.
#  'a'     append          Append only. Creates file if not found.
#                          Adds to end. Does NOT delete existing content.
#  'x'     create          Creates a new file. Error if file EXISTS.
#  't'     text            Text mode (default). Used with r, w, a.
#  'b'     binary          Binary mode. Used with r, w, a for non-text files.
#  'r+'    read + write    Read and write. Error if file not found.
#  'w+'    write + read    Read and write. DELETES existing content.
#  'a+'    append + read   Read and append. Does NOT delete content.
#
# Modes can be combined: 'rb', 'wt', 'a+' etc.
# Default mode if nothing is passed: 'r' (read, text mode)
# ============================================================


# ============================================================
#                  MODE 'r' -- READ
# ============================================================
# Opens file for READING only.
# Raises FileNotFoundError if the file does not exist.
# Default mode -- 'r' and 'rt' are identical.
# Cannot write to a file opened in 'r' mode.

# f = open('myfile.txt', 'r')   # FileNotFoundError if not found

f = open('file_handling.txt', 'r')
text = f.read()
print(text)
f.close()

# 'r' is the default so this works the same way:
# f = open('file_handling.txt')

# RECOMMENDED -- using 'with' so file closes automatically:
with open('file_handling.txt', 'r') as f:
    text = f.read()
    print(text)
# file is closed here automatically -- even if an error occurred


# ------------------------------------------------------------
# Reading methods -- different ways to read a file
# ------------------------------------------------------------

with open('file_handling.txt', 'r') as f:
    content = f.read()          # reads the ENTIRE file as one string
    print(content)

with open('file_handling.txt', 'r') as f:
    line = f.readline()         # reads ONE line at a time
    print(line)

with open('file_handling.txt', 'r') as f:
    lines = f.readlines()       # reads ALL lines into a LIST
    print(lines)                # ['line1\n', 'line2\n', 'line3\n']

# looping line by line -- most memory efficient for large files:
with open('file_handling.txt', 'r') as f:
    for line in f:
        print(line.strip())     # strip() removes the \n at the end


# ============================================================
#                  MODE 'w' -- WRITE
# ============================================================
# Opens file for WRITING only.
# If file does NOT exist -- creates it.
# If file DOES exist -- DELETES all existing content and rewrites.
# Cannot read from a file opened in 'w' mode.
# RULE: use 'w' only when creating a brand new file.
#       use 'a' when adding to an existing file.

f = open('file_handling.txt', 'w')
f.write('Hi i am using mode w to test')
f.close()

# RECOMMENDED -- using 'with':
with open('file_handling.txt', 'w') as f:
    f.write("testing 'with' statement with mode 'w'\n")
    f.write("second line written here\n")   # call write() multiple times
# file is automatically closed and saved here


# ============================================================
#                  MODE 'a' -- APPEND
# ============================================================
# Opens file for APPENDING only.
# If file does NOT exist -- creates it.
# If file DOES exist -- adds to the END without deleting anything.
# Cannot read from a file opened in 'a' mode.
# RULE: use 'a' when you want to add new data to an existing file.

f = open('file_handling.txt', 'a')
f.write('Hi i am using mode a to test')
f.close()

# RECOMMENDED -- using 'with':
with open('file_handling.txt', 'a') as f:
    f.write("\nnew line appended here")     # \n moves to next line first
# existing content is preserved, new line added at the end


# ============================================================
#                  MODE 'x' -- CREATE
# ============================================================
# Creates a BRAND NEW file.
# Raises FileExistsError if the file already exists.
# Useful when you want to make sure you never overwrite an existing file.
# 'w' silently overwrites -- 'x' refuses and raises an error instead.

# f = open('file_handling2.txt', 'x')
# f.write('Hi i am using mode x to test')
# f.close()

# safe creation using 'with':
# with open('newfile.txt', 'x') as f:
#     f.write('this file did not exist before')


# ============================================================
#                  MODE 't' -- TEXT
# ============================================================
# Text mode -- the DEFAULT mode when no mode is specified.
# 'r' and 'rt' are identical. 'w' and 'wt' are identical.
# Used for plain text files (.txt, .csv, .json, .py etc.)
# Returns content as a Python STRING.

f = open('file_handling.txt', 'rt')
text = f.read()
print(text)             # output is a string
f.close()


# ============================================================
#                  MODE 'b' -- BINARY
# ============================================================
# Binary mode -- used for non-text files.
# Used for: images, PDFs, audio, video, executables etc.
# Returns content as BYTES, not a string.
# You will see output like: b'some content here'
# The b prefix means it is a bytes object, not a regular string.

f = open('file_handling.txt', 'rb')
text = f.read()
print(text)             # b'Hi i am using mode...'  <- bytes object
f.close()

# common use -- copying an image file:
# with open('photo.jpg', 'rb') as source:
#     data = source.read()
# with open('photo_copy.jpg', 'wb') as dest:
#     dest.write(data)


# ============================================================
#              MANUAL close() vs 'with' STATEMENT
# ============================================================
# Manual -- you must remember to call close() every time:
f = open('file_handling.txt', 'r')
text = f.read()
f.close()               # if this is forgotten, file stays locked

# with statement -- closes automatically no matter what:
with open('file_handling.txt', 'r') as f:
    text = f.read()
# no need to call close() -- Python handles it here

# WHY 'with' IS BETTER:
# If an error occurs between open() and close() in the manual approach,
# close() never runs -- the file stays open and locked.
# 'with' guarantees the file is closed even if an error crashes the code.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Mode    Creates?   Deletes Existing?   Read?   Write?
#  ──────────────────────────────────────────────────────────
#  'r'     No         No                  Yes     No
#  'w'     Yes        YES -- careful      No      Yes
#  'a'     Yes        No                  No      Yes
#  'x'     Yes        Error if exists     No      Yes
#  'r+'    No         No                  Yes     Yes
#  'w+'    Yes        YES -- careful      Yes     Yes
#  'a+'    Yes        No                  Yes     Yes
#  't'     (default, combine with r/w/a)
#  'b'     (binary,  combine with r/w/a)
#
#  Reading methods:
#  ──────────────────────────────────────────────────────────
#  read()          Entire file as one string
#  readline()      One line at a time
#  readlines()     All lines as a list
#  for line in f   Loop line by line -- best for large files
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────
#  1. Always use 'with' -- it closes the file automatically
#  2. 'w' DELETES existing content -- use 'a' to preserve it
#  3. 'x' is safer than 'w' when creating -- errors if file exists
#  4. Text mode returns strings, binary mode returns bytes
#  5. Use strip() when reading lines to remove trailing newlines
#
# ============================================================
