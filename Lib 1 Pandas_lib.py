'''
Pandas - basic understanding
'''

import numpy as np
import pandas as pd

dict_info = {
    'name' : ['Ujjwal', 'Roham', 'Pooja', 'Prem', 'Power'],
    'Age' : [25,17,28,19,21],
    'City' : ['DELHI', 'PUNJAB', 'HARAYANA' , ' MAHARASHTRA' , 'GOA']
}

# dataframe method wll create a excel sheet structure to the organised data
df  = pd.DataFrame(dict_info)
print(df)

'''
Output: here the 0 to 4 are indexing or rows, obviosly starts from 0 
and name, age, city are keys from dict become columns 
and the respective values has been structured into excel sheet like structure
this is what dataframe do
    name  Age          City
0  Ujjwal   25         DELHI
1   Roham   17        PUNJAB
2   Pooja   28      HARAYANA
3    Prem   19   MAHARASHTRA
4   Power   21           GOA
'''

# df.to_csv()
'''
this will convert the df created from the data set to csv file and save with whatever name user wants 
and at whatever location in the system, it will be in CSV format
'''
df.to_csv('Sample_Testing.csv')

# and if you dont want the index or row numbers as shown like this:
'''
    name  Age          City
0  Ujjwal   25         DELHI
1   Roham   17        PUNJAB
2   Pooja   28      HARAYANA
3    Prem   19   MAHARASHTRA
4   Power   21           GOA

then do this, this will remove the indexing 
'''
df.to_csv('Sample_Testing.csv', index=False)


'''
this is the work with small dataset

lets say we have data set with millions of row and we need to check firt or last n rows

then
'''
# this will give the first 2 rows
print(df.head(2))

# this will gice the last 2 rows
print(df.tail(2))


'''
describe() - this method will give you a statistical report for a all the numarical columns in the dataset
for example: we only have age as numerical column

output of the below code - print(df.describe())

           Age
count   5.000000
mean   22.000000
std     4.472136
min    17.000000
25%    19.000000
50%    21.000000
75%    25.000000
max    28.000000


these functions describe will perform on numerical columns
'''
print(df.describe())

# read_csv()
'''
this will read a particular csv, it is a built in pandas function
'''
uj = pd.read_csv('Sample_Testing.csv')
print(uj)

# accessing the rows and column of a df/or readed_csv
'''
to access the elements in the df, we can use rows and column

for row use indexing to get access of the rows
for columns use column name to get access of the particular column data
'''

# access based on column names
print(uj['Age'])

#access based on specific value using column name and indxing of rows
# not a recommended method as this will show a warning but it will work
print(uj['Age'][0])  #shows the value at 0th indexing which is first row at column ages

# updating a value on a specific position, perform to.csv() with the same name and 
# after updating and it will then also update in the same csv
uj['Age'][0] = 99
print(uj['Age'])

# changing the indexing from 0 to n to anything 
# but it is not efficient way to do it as this can possibly lead to - ValueError: Length mismatch: Expected axis has 5 elements, new values have 3 elements
# for example, 
uj.index = ['first','second','third','fourth','fifth']
print(uj)
