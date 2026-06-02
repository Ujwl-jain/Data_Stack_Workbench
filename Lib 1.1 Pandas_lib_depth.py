'''
Pandas - Depth

it is a open source lib, better than excel it provides more function then excel itself

used for analysis, if the dataset comes in programming then analysis can become easy using pandas

it used the speed and power of numpy, as numpy is fast and gives better storage.

its two types:
series: it is a 1D array with indexes, it stores single row or column of data in dataframe, combination of series creates a dataframe

dataframe: tabular representation like excel sheet structure representing multiple rows and columns for performaing many data analysis task
'''

# Series 
'''
series written as 'Series', 

this is a data structure of pandas just like list, tuple and dict is for python 
'''

import pandas as pd
import numpy as np
from random import random

# this will give a series of data till indexing 34, which is from 0 to 33 with random number using random
ser = pd.Series(np.random.rand(34))
# print(ser)
print(type(ser))

# Dataframe
'''
Dataframe

'''
# this will provide a sample data of random nmbers with 0-99(100 as indexing) rows, and 5 columns(0-4)
newdf = pd.DataFrame(np.random.rand(100,5), index = np.arange(100))

# prints(the entire df)
# print(newdf)

# prints the first 5 rows of df
print(newdf.head())
print(type(newdf))

# describe on df
print(newdf.describe())

# dtypes - 
# it shows the data types of each column as it can differ even if 1 value is different in one particular column
# for example: if a at any column at any position there is a string and all other data is int or float,
# then the dtype of that column is object type while others who have the data in int or float will show int or float
'''
showing each colum has float datatype
0    float64
1    float64
2    float64
3    float64
4    float64
dtype: object

lets say column one has string at 1st row, then this will be how its datatype looks like

0    float64
1     object
2    float64
3    float64
4    float64
dtype: object

Overall, dataframe is of dtype object

PS: if there is a string in any columns then 
if you perform describe() then it will left that column which contains string and 
perform the describe() on all other columns
'''

print(newdf.dtypes)

# newdf[1][1] = 'Ujjwal'
print(newdf.head())
print(newdf.dtypes)


# index() - rows, columns - column
print(newdf.index)
print(newdf.columns)

# converting into numpy array
print(newdf.to_numpy())


# --------------------- attributes ---------------------------
# transpone - it will transpose the df. where row becomes columna and column become rows, just like transposing a matrix
# print(newdf.T.head())

# ------------
# Indexing sort
'''
sort the indexing as per user desire:

axis = 0 means, sorting based on rows
axis = 1 means, sorting based on columns

ascending is by default true, doing false will make the rows or column shows in df in descending order
'''
print(newdf.sort_index(axis = 0, ascending=False))
print(newdf.sort_index(axis = 1, ascending=False))

# ------------
# accessing a column
'''
# this will access the column 0 or first column and shows each data on row, and 
# its dtype will come as series, means a combination of series creates a Dataframe
# since first column name was 0 that is how we used 0 else 
# if it is string, then we will use the name of the column like this 'column name', overall accessing a column can be done using the name of the column
'''
print(newdf[0])
print(type(newdf[0]))

# ------------
# copy a df
'''
this is not a copy of df but a view same as original df

for example:
we put the view of original df to 2nd df, and 
if we changed anything inside 2nd df, then the original df will be changed too

it is preferable to use copy()
'''
newdf2 = newdf
print(newdf2.head())
newdf2[0][0] = 98.97
print(newdf.head())
print(newdf2.head())

# this will make a copy of df to another df and if you changed in copied version then the original will not change
# newdf3 = newdf[:]
# newdf3 = newdf.copy()

# ------------
# changing column names
newdf.columns = list("ABCDE")
# print(newdf.head(2))

# ------------
# drop
'''
it drops a particular column or row, if axis = 1 and its name is 0 then it will remove from column side,
it is a different story if column name differs from indexing, as it will give error if we did not provide the axis for column
cause by default drop checks from row and if the name not found in indexing then it will give error

this will drop from the original df,
'''
# delete from column which has a name 0
# newdf = newdf.drop(0, axis = 1)
# or
# newdf = newdf.drop('A', axis = 1)
# newdf = newdf.drop(['A','C'], axis = 1)
# print(newdf.head(2))

# # delete from rows which is 0
# newdf = newdf.drop(0, axis = 0) 
# # or
# print(newdf.head(2))
# newdf = newdf.drop(0)
# print(f'droping rows {newdf}')

'''
for not changing the orignal df and applying this function do this

bascially this will apply and print the changes doen without changing the original dataset, 
one can say, it is just a view after apply a function
'''
# for rows
# print(newdf.drop([0], axis = 0))
# or by default axis is 0
# print(newdf.drop([0]))

# for columns
# use the indexing and axis
# print(newdf.drop([0], axis = 1 ))
# or, use the column name and axis 
# newdf.drop(['A','C'], axis = 1)
# print(newdf.drop(['A'], axis = 1))

'''
but using inplace(), function we can also remove the desried row and column from the original df

inplace() basically made changes inside the original df
'''

# for rows
# print(newdf.drop([0], axis = 0, inplace = True))
# or by default axis is 0
# print(newdf.drop([0]))

# for columns
# use the indexing and axis
# print(newdf.drop([0], axis = 1, inplace = True))
# or, use the column name and axis 
# newdf.drop(['A','C'], axis = 1, inplace = True)
# print(newdf.drop(['A'], axis = 1, inplace = True))

'''but after dropping rows like we remove the 1,3 row 
then the indexing in df looks like 0,2,4,5 which looks inaccurate
which can confusing during analysis of df.

to correct this we can use reset_index()
this will reset the index  by adding a column naming index with correct numbers

and if you dont need new column to be added then do this reset_index(drop = True)
this will remove the index column and indexing also will be accurate
'''

# newdf.reset_index()
# newdf.reset_index(drop =True, inplace = True)
# or
# newdf = newdf.reset_index(drop =True)

# ------------
# loc function
'''
where you can select the data of row or column with there name
where 0 = indexing or row number, and A is the name of the column
'''
newdf.loc[0,'A'] = 654
print(newdf.head(2))

'''
if want to access only specific column or row then

this will show the first 2 rows and C,D columns of the dataframe, as a new dataframe
this will not change the original df for that we have to write newdf = newdf.loc[[1,2],['C','D']]
'''
print(newdf.loc[[1,2],['C','D']])
print(newdf)

# performing slicing
# will give all rows with C,D columns
newdf.loc[:,['C','D']]

# will give all columns with 1,2 rows
newdf.loc[[1,2],:]

# complex query runinng using df

'''
just like we perfom query in DB we can do this here aswell
for example
'''
print(newdf.loc[(newdf['B'] < 0.3)])

print(newdf.loc[(newdf['A']< 0.3) & (newdf['C'] > 0.1)])

# ------------
# iloc function
'''
Similar to loc, but

print(newdf.iloc[0,4])
basically it will access the data of 0th row and 5th column 
as counting starts from 0 then 4th will become 5th in dataset

if we want to see the dataset of of particular columns or row no matter the names of the column
then we will use 'iloc' providng the indexing range
for exaample [0,4] will show us the data of 1 row and 5 th column

and if we want to check the dataset for columns using names then use 'loc'
'''
print(newdf.head(2))
print(newdf.loc[[1,2],['B']])
print(newdf.iloc[0,4])
print(newdf.iloc[[0,1], [1,2]])

# ----------------------------------------
# difference between loc and iloc
'''
loc vs iloc

loc — Label Based
You access data using the actual names — column names and index labels.

iloc — Integer Position Based
You access data using position numbers — like indexing into a list, always 0, 1, 2, 3...

When to use which:
Use loc when you know the name of what you want — a column called 'B', a row with index 1. This is what you will use 90% of the time in real work.
Use iloc when you care about position — the first 5 rows, the last column, the 3rd to 7th rows. Useful when column names are unknown or when you are working positionally like slicing a list.

the two lists are not coordinate pairs — print(newdf.iloc[[0,1], [1,2]])

rows    = [0, 1]       → row at position 0, row at position 1
columns = [1, 2]       → column at position 1, column at position 2

result = every row crossed with every column:

         col 1      col 2
row 0 → 0.337599   0.806300
row 1 → 0.562250   0.707983

This is called a cross product — all rows against all columns. That is why you get a 2x2 block, not just 2 individual values.

they are independently selecting which rows and which columns to include, and 
then the result is every combination of those rows and columns together.

# ============================================================
#                     loc vs iloc IN PANDAS
# ============================================================
# Both are used to access rows and columns in a DataFrame.
#
# loc  -- LABEL based  -- uses actual index values and column names
# iloc -- INTEGER based -- uses position numbers (always 0, 1, 2...)
#
# SYNTAX:
#   df.loc[row_label,    column_name]
#   df.iloc[row_position, col_position]
# ============================================================
# sample dataframe -- NOTE: index starts from 1, not 0
# this is important to understand the loc vs iloc difference
df = pd.DataFrame(np.random.rand(3, 4), columns=['A','B','C','D'], index=[1,2,3])

#      A         B         C         D
# 1  0.52...   0.33...   0.80...   0.11...
# 2  0.22...   0.56...   0.44...   0.70...
# 3  0.71...   0.91...   0.22...   0.53...


# ============================================================
#                          loc
# ============================================================
# Uses ACTUAL LABELS -- column names and real index values.
# If your index is [1,2,3], you must use 1,2,3 -- not 0,1,2.
# Slice stop is INCLUSIVE.

# single value -- row labeled 1, column named 'A':
print(df.loc[1, 'A'])

# modify a value:
df.loc[1, 'A'] = 654

# specific rows and columns by name:
print(df.loc[[1,2], ['C','D']])     # rows labeled 1 and 2, columns C and D

# all rows, selected columns:
print(df.loc[:, ['C','D']])

# all columns, selected rows:
print(df.loc[[1,2], :])

# slice -- rows 1 to 2, all columns (STOP IS INCLUSIVE in loc):
print(df.loc[1:2, :])               # includes row labeled 2

# conditional filtering -- like WHERE clause in SQL:
print(df.loc[df['B'] < 0.3])
print(df.loc[(df['A'] < 0.3) & (df['C'] > 0.1)])


# ============================================================
#                         iloc
# ============================================================
# Uses POSITION NUMBERS -- always 0, 1, 2... no matter what
# the actual index labels are.
# Slice stop is EXCLUSIVE -- just like Python lists.

# single value -- row at position 0, column at position 3:
print(df.iloc[0, 3])

# block of cells -- rows at positions 0,1 AND columns at positions 1,2:
print(df.iloc[[0,1], [1,2]])
# rows [0,1] and columns [1,2] are TWO SEPARATE LISTS
# result is every combination -- a 2x2 block, not just 2 cells

# all rows, first 2 columns:
print(df.iloc[:, 0:2])              # stop 2 is EXCLUSIVE -- gives col 0 and 1 only

# first 2 rows, all columns:
print(df.iloc[0:2, :])              # stop 2 is EXCLUSIVE -- gives row 0 and 1 only


# ============================================================
#         THE KEY DIFFERENCE -- same df, different result
# ============================================================
# If index is [1, 2, 3] (starts from 1):

print(df.loc[1, 'A'])       # row LABELED 1  -- first row
print(df.iloc[0, 0])        # row at POSITION 0 -- also first row
# both point to the same cell here

# but if index was [10, 20, 30]:
# df.loc[10, 'A']   -- works, finds label 10
# df.iloc[0, 0]     -- works, finds position 0 (which is label 10)
# df.loc[0, 'A']    -- KeyError -- no label 0 exists in the index


# ============================================================
#              SINGLE VALUE vs BLOCK -- iloc rule
# ============================================================

print(df.iloc[0, 3])            # two single ints   -> ONE cell
print(df.iloc[[0,1], [1,2]])    # two lists         -> 2x2 block
print(df.iloc[:, [0,1]])        # all rows, 2 cols  -> block
print(df.iloc[[0,1], :])        # 2 rows, all cols  -> block


# ============================================================
#                   QUICK REFERENCE SUMMARY
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
#  Bracket rules for iloc:
#  ──────────────────────────────────────────────────────────────
#  iloc[int, int]          single cell
#  iloc[[ints], [ints]]    block -- all row positions x all col positions
#  iloc[:, [ints]]         all rows, selected columns
#  iloc[[ints], :]         selected rows, all columns
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────
#  1. loc uses labels  -- iloc uses positions, always starting from 0
#  2. loc slice stop is inclusive -- iloc slice stop is exclusive
#  3. iloc lists are NOT coordinate pairs -- they are rows x columns
#  4. When index starts from 1, loc[1] != iloc[1] -- they are different rows
#  5. Use loc 90% of the time -- use iloc when position matters more than name
#
# ============================================================
'''

# ---------------
# Some functions to perform
# isnull() will show where the values are null or none
newdf['A'].isnull()

# changing the entire dataset of a column:
# can be done using this but prefreable is
newdf['B'] = None

# but this prefreabl: cause in real time projects there might be a confusiog  
# where you might need to change the datset, and it can be either view or copy 
# it is difficult to understand at that point so to be safe use loc or iloc
newdf.loc[:, ['B']] = None
newdf['B'].isnull()
newdf.loc[:, ['B']] = 34

# -------------------------------
df = pd.DataFrame(
    {
        "name": ["Alfred", "Batman", "Catwoman"],
        "toy": [np.nan, "Batmobile", "Bullwhip"],
        "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
    }
)

print(df.head)

# newdf.dropna()
# newdf.drop_duplicates()
# new.df.value_count()
# newdf.info()
# newdf.notnull()
