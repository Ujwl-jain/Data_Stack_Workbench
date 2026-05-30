# ============================================================
#                     PANDAS IN PYTHON
# ============================================================
# Pandas is an open-source library for data analysis.
# Better than Excel -- more functions, handles millions of rows,
# programmable, and faster due to NumPy under the hood.
#
# TWO CORE DATA STRUCTURES:
#   Series    -- 1D array with index (single row or column)
#   DataFrame -- 2D table with rows and columns (like Excel sheet)
#               A DataFrame is just a collection of Series combined.
#
# INSTALL: pip install pandas
# IMPORT:  import pandas as pd
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
#                        SERIES
# ============================================================
# A 1D labeled array -- like a single column of a spreadsheet.
# Has an index (labels for each value) and the values themselves.

ser = pd.Series(np.random.rand(5))
print(ser)
print(type(ser))        # <class 'pandas.core.series.Series'>

# Output looks like:
# 0    0.452
# 1    0.891
# 2    0.123
# 3    0.674
# 4    0.345
# dtype: float64
# left side = index, right side = values


# ============================================================
#                       DATAFRAME
# ============================================================
# A 2D table -- rows and columns like an Excel sheet.
# Created from a dictionary where:
#   keys   = column names
#   values = list of column data

dict_info = {
    'name': ['Ujjwal', 'Roham', 'Pooja', 'Prem', 'Power'],
    'Age':  [25, 17, 28, 19, 21],
    'City': ['DELHI', 'PUNJAB', 'HARAYANA', 'MAHARASHTRA', 'GOA']
}

df = pd.DataFrame(dict_info)
print(df)
# Output:
#      name  Age         City
# 0  Ujjwal   25        DELHI
# 1   Roham   17       PUNJAB
# 2   Pooja   28     HARAYANA
# 3    Prem   19  MAHARASHTRA
# 4   Power   21          GOA
#
# 0-4 on the left = row index (auto-assigned from 0)
# name, Age, City = column names from dict keys

# creating df with random data:
newdf = pd.DataFrame(np.random.rand(100, 5), index=np.arange(100))
print(newdf.head())     # first 5 rows


# ============================================================
#                  BASIC EXPLORATION
# ============================================================

# head() and tail() -- see first or last n rows:
print(df.head(2))       # first 2 rows
print(df.tail(2))       # last 2 rows
print(newdf.head())     # default = 5 rows

# describe() -- statistical summary of ALL numerical columns:
print(df.describe())
# Output:
#         Age
# count   5.0     <- number of rows
# mean   22.0     <- average
# std     4.47    <- standard deviation (how spread out values are)
# min    17.0     <- smallest value
# 25%    19.0     <- 25th percentile (Q1)
# 50%    21.0     <- median (Q2)
# 75%    25.0     <- 75th percentile (Q3)
# max    28.0     <- largest value
# NOTE: string columns are ignored by describe()

# dtypes -- data type of each column:
print(newdf.dtypes)
# if a column has even ONE string value, its dtype becomes 'object'
# all-numeric columns show float64 or int64
# Overall df dtype is always 'object'

# index and columns -- see row labels and column names:
print(newdf.index)      # RangeIndex(start=0, stop=100, step=1)
print(newdf.columns)    # Index([0, 1, 2, 3, 4], dtype='int64')

# info() -- quick overview of df: shape, dtypes, non-null counts:
# newdf.info()

# to_numpy() -- convert df to a numpy array:
print(newdf.to_numpy())


# ============================================================
#                  READING AND WRITING FILES
# ============================================================

# to_csv() -- save df as a CSV file:
df.to_csv('Sample_Testing.csv')             # with index column
df.to_csv('Sample_Testing.csv', index=False)  # without index column
# index=False removes the 0,1,2... column from the saved file
# use this when you don't want row numbers saved into the file

# read_csv() -- load a CSV file into a df:
uj = pd.read_csv('Sample_Testing.csv')
print(uj)


# ============================================================
#                  ACCESSING DATA
# ============================================================

# access a full column by name -- returns a Series:
print(uj['Age'])
print(type(uj['Age']))      # <class 'pandas.core.series.Series'>

# access a specific cell -- column name + row index:
print(uj['Age'][0])         # value at row 0, column Age
# NOTE: this works but raises a warning -- use loc/iloc instead

# updating a cell value:
uj['Age'][0] = 99           # works but warning -- prefer loc
uj.loc[0, 'Age'] = 99       # correct way

# changing column names all at once:
newdf.columns = list("ABCDE")   # renames columns 0,1,2,3,4 to A,B,C,D,E
print(newdf.head(2))

# changing index labels:
uj.index = ['first', 'second', 'third', 'fourth', 'fifth']
print(uj)
# WARNING: new index list must have SAME length as df rows
# otherwise ValueError: Length mismatch


# ============================================================
#                   COPYING A DATAFRAME
# ============================================================
# WRONG way -- this creates a VIEW, not a copy:
newdf2 = newdf
newdf2[0][0] = 98.97        # modifies newdf2
print(newdf.head())         # original ALSO changed -- they share memory

# CORRECT way -- use copy():
newdf3 = newdf.copy()       # fully independent copy
newdf3.loc[0, 'A'] = 0      # modifies only newdf3
print(newdf.head())         # original unchanged

# also works:
# newdf3 = newdf[:]         # slice copy -- also independent


# ============================================================
#                     TRANSPOSE
# ============================================================
# Rows become columns, columns become rows -- same as matrix transpose.

print(newdf.T.head())


# ============================================================
#                     SORT INDEX
# ============================================================
# sort_index() -- sort rows or columns by their labels.
# axis=0 = sort rows by index label
# axis=1 = sort columns by column name
# ascending=False = descending order

print(newdf.sort_index(axis=0, ascending=False))    # rows in reverse order
print(newdf.sort_index(axis=1, ascending=False))    # columns Z to A


# ============================================================
#                       DROP
# ============================================================
# Removes rows or columns from the df.
# axis=0 = drop rows (default)
# axis=1 = drop columns
#
# By default drop() does NOT modify the original df.
# It returns a new df with the row/column removed.
# To modify original, either reassign or use inplace=True.

# drop a column -- must specify axis=1:
newdf.drop('A', axis=1)                     # view only, original unchanged
newdf = newdf.drop('A', axis=1)             # reassign to apply
newdf.drop(['A', 'C'], axis=1, inplace=True)  # inplace modifies original directly

# drop a row -- axis=0 is default:
newdf.drop(0, axis=0)           # drop row with index label 0
newdf.drop([0, 1])              # drop rows 0 and 1 (axis=0 by default)

# after dropping rows, index becomes [2,3,4,5...] -- gaps appear
# fix this with reset_index():
newdf.reset_index(drop=True, inplace=True)
# drop=True   = removes the old index, does not add it as a column
# inplace=True = modifies original df directly
# without drop=True, old index becomes a new column named 'index'


# ============================================================
#                    NULL VALUES
# ============================================================
# Real datasets have missing values -- pandas handles them as NaN or NaT.
# NaN  = Not a Number (missing numerical value)
# NaT  = Not a Time (missing datetime value)

df_null = pd.DataFrame({
    "name": ["Alfred", "Batman", "Catwoman"],
    "toy":  [np.nan, "Batmobile", "Bullwhip"],
    "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
})
print(df_null)

# isnull() -- returns True where value is NaN/NaT:
print(newdf['A'].isnull())

# notnull() -- opposite of isnull():
# print(newdf['A'].notnull())

# dropna() -- remove rows that contain ANY null value:
# newdf.dropna()

# fillna() -- fill null values with something instead of dropping:
# newdf.fillna(0)           # fill all NaN with 0
# newdf['A'].fillna(newdf['A'].mean())  # fill with column average

# setting a column to None -- two ways:
newdf.loc[:, ['B']] = None      # preferred -- safe, no ambiguity
# newdf['B'] = None             # works but may cause SettingWithCopyWarning

# setting back to a value:
newdf.loc[:, ['B']] = 34


# ============================================================
#                    loc -- LABEL BASED ACCESS
# ============================================================
# Access rows and columns using their ACTUAL LABELS.
# Column names like 'A', 'B' and real index values like 0, 1, 2.
# Slice stop is INCLUSIVE.
# Supports conditional filtering.

newdf.loc[0, 'A'] = 654                     # modify single cell
print(newdf.loc[[1, 2], ['C', 'D']])        # rows labeled 1,2 -- columns C,D
print(newdf.loc[:, ['C', 'D']])             # all rows, columns C and D
print(newdf.loc[[1, 2], :])                 # rows 1,2 -- all columns
print(newdf.loc[1:2, :])                    # slice rows 1 to 2 INCLUSIVE

# conditional filtering -- like WHERE in SQL:
print(newdf.loc[newdf['B'] < 0.3])
print(newdf.loc[(newdf['A'] < 0.3) & (newdf['C'] > 0.1)])


# ============================================================
#                    iloc -- POSITION BASED ACCESS
# ============================================================
# Access rows and columns using POSITION NUMBERS 0, 1, 2...
# Always 0-based regardless of actual index labels.
# Slice stop is EXCLUSIVE -- same as Python lists.
# Does NOT support conditional filtering.

print(newdf.iloc[0, 4])             # single cell -- row 0, col 4
print(newdf.iloc[[0, 1], [1, 2]])   # block -- rows 0,1 crossed with cols 1,2

# HOW THE BLOCK WORKS:
# rows    = [0, 1]  -- row at position 0 and row at position 1
# columns = [1, 2]  -- col at position 1 and col at position 2
# result  = EVERY combination -- 2x2 block (not just 2 individual cells)
#          col1       col2
# row0  → value      value
# row1  → value      value

print(newdf.iloc[:, 0:2])           # all rows, cols 0 and 1 (2 is excluded)
print(newdf.iloc[0:2, :])           # rows 0 and 1, all cols (2 is excluded)


# ============================================================
#                    loc vs iloc -- SUMMARY
# ============================================================
#
#  Feature              loc                      iloc
#  ──────────────────────────────────────────────────────────────
#  Based on             Labels and names         Position numbers
#  Row access           Actual index value       0, 1, 2...
#  Column access        Column name ('A','B')    0, 1, 2...
#  Slice stop           INCLUSIVE                EXCLUSIVE
#  Conditional filter   Yes                      No
#  Use when             You know the name        You know the position
#
#  iloc bracket rules:
#  iloc[int, int]          -> single cell
#  iloc[[ints], [ints]]    -> block (rows x columns cross product)
#  iloc[:, [ints]]         -> all rows, selected columns
#  iloc[[ints], :]         -> selected rows, all columns


# ============================================================
#                   OTHER USEFUL FUNCTIONS
# ============================================================

# value_counts() -- count occurrences of each unique value in a column:
# newdf['A'].value_counts()

# drop_duplicates() -- remove duplicate rows:
# newdf.drop_duplicates()

# sort_values() -- sort df by values in a column:
# newdf.sort_values('A', ascending=False)

# groupby() -- group rows by a category and apply aggregation:
# newdf.groupby('Dept')['Salary'].sum()

# merge() -- join two dataframes like SQL JOIN:
# pd.merge(df1, df2, on='common_column')


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Creation:
#  ──────────────────────────────────────────────────────────────
#  pd.DataFrame(dict)          Create df from dictionary
#  pd.DataFrame(np.array)      Create df from numpy array
#  pd.read_csv('file.csv')     Load CSV into df
#  pd.Series(array)            Create a 1D series
#
#  Exploration:
#  ──────────────────────────────────────────────────────────────
#  df.head(n)                  First n rows (default 5)
#  df.tail(n)                  Last n rows (default 5)
#  df.describe()               Statistical summary (numerical only)
#  df.dtypes                   Data type of each column
#  df.info()                   Shape, dtypes, non-null counts
#  df.index                    Row labels
#  df.columns                  Column names
#  df.shape                    (rows, columns) as tuple
#  df.size                     Total number of cells
#
#  Modification:
#  ──────────────────────────────────────────────────────────────
#  df.to_csv('f.csv')          Save df to CSV
#  df.copy()                   Independent copy of df
#  df.columns = [...]          Rename all columns
#  df.drop('col', axis=1)      Drop a column (view)
#  df.drop(0, axis=0)          Drop a row (view)
#  df.drop(..., inplace=True)  Drop and modify original
#  df.reset_index(drop=True)   Fix index after dropping rows
#  df.sort_index(axis, asc)    Sort by index labels
#  df.T                        Transpose rows and columns
#  df.to_numpy()               Convert to numpy array
#
#  Null handling:
#  ──────────────────────────────────────────────────────────────
#  df.isnull()                 True where value is NaN/NaT
#  df.notnull()                True where value is NOT null
#  df.dropna()                 Remove rows with any null
#  df.fillna(value)            Replace nulls with a value
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Use df.copy() not df2=df -- assignment creates a view not a copy
#  2. Use loc/iloc to modify values -- avoid df['col'][row] pattern
#  3. drop() does not modify original by default -- reassign or inplace=True
#  4. reset_index(drop=True) after dropping rows to fix index gaps
#  5. describe() skips string/object columns automatically
#  6. index list in df.index = [...] must match exact row count
#
# ============================================================