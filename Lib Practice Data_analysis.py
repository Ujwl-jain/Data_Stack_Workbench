# Libraries to be imported
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In built dataset
# df = sns.load_dataset('titanic')   # passenger survival data
# df = sns.load_dataset('iris')      # flower measurements
df_data = sns.load_dataset('tips')      # restaurant tips data


# ==================== TIPS ===========================

# simple options to perform
'''
to_string() is used to print all rows and columns as view
dtypes is used to check the types of each column
.column is used to check for all the columns in the data frame
'''
print(df_data.to_string())

print('------------------------------------------------------------------')
print(f"Following is the practice for dtype():\n", df_data.dtypes)

print('------------------------------------------------------------------')
# Q1. How many rows and columns does the tips dataset have?
# What you learn: df.shape, understanding dataset size
# Hint: .shape
'''
Ans: According to output there are 7 columsna and 244 rows

No of columns are: Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='str')
No of rows RangeIndex(start=0, stop=244, step=1)
No of rows and columns as size (244, 7)
'''

print(f"No of columns are:", df_data.columns)
print(f"No of rows", df_data.index)
print("No of rows and columns as size", df_data.shape)

print('------------------------------------------------------------------')
# Q2. What are the data types of each column?
# What you learn: spotting which columns are numeric vs categorical
# Hint: .dtypes
'''
Ans : ther are total 7 columns:

Types of columns exist in the dataframe: 
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object

The total count for each dtype is: 
float64     2
category    1
category    1
category    1
category    1
int64       1

value_count(), count the value of each dtypes and return the count
'''
print("Types of columns exist in the dataframe: \n", df_data.dtypes)
print("The total count for each dtype is: \n", df_data.dtypes.value_counts() )


print('------------------------------------------------------------------')
# Q3. Are there any missing values in the dataset?
# What you learn: always check this before any analysis
# Hint: .isnull().sum()
'''
The total null values present in the Df: 
 total_bill    0
tip           0
sex           0
smoker        0
day           0
time          0
size          0
dtype: int64

there are total 0  null values inside a dataset of any columns
'''
# if we dont do sum then it will either return true or false, false for not containing null, true for containing
df_not_sum = df_data.isnull()

# for doing .sum() it will calculate the total nuumber of appearence of True values in a column
df_null = df_data.isnull().sum()
print(f'The total null values present in the Df: \n', df_null)

print('------------------------------------------------------------------')
# Q4. What is the average tip amount?
# What you learn: .mean() on a column
# Hint: df['tip'].mean()
'''
Below approach is simple to check the mean of a column using column name

2nd approach is, to loop through each column, and check if dtype is this and if yes then apply mean

pd.api.types.is_numeric_dtype():

this means that it will check whether the column is numeric or not, as for now it is int64 or float64,
but in real data set it can be anything like int8, int32, float8... etc, this will just check whether it is numeric means either int or float

for more refer to Panda_New_Topics.py
'''
df_mean_for_a_column = df_data['tip'].mean()

for col in df_data.columns:
    if df_data[col].dtype == 'int64' or df_data[col].dtype == 'float64':
        print(f"The mean for all the following {col} are:", df_data[col].mean())

# using pd.api.types.is_numeric_dtype()
for col in df_data.columns:
    if pd.api.types.is_numeric_dtype(df_data[col]):
        print(f"The mean for all the following {col} are using pd.api.types.is_numeric_dtype():", df_data[col].mean())

# df_mean_for_a_df = df_data.mean()
# print(f"The mean for all the following columns are:", df_mean_for_a_df)
print(f"The mean for all the following columns are:", df_mean_for_a_column)


print('------------------------------------------------------------------')
# Q5. What is the highest total bill ever recorded?
# What you learn: .max()

'''
here we are going to get the maximum for each colum as well as well as the total bill
'''

for col in df_data.columns:
    if pd.api.types.is_numeric_dtype(df_data[col]):
        print(f"The max value from the {col} is: ", df_data[col].max())


print(f"the following max value for Total bill is: ", df_data['total_bill'].max())

print('------------------------------------------------------------------')
# Q6. How many male vs female customers are there?
# What you learn: .value_counts()
# Hint: df['sex'].value_counts()

for col in df_data.columns:
    if pd.api.types.is_string_dtype(df_data[col]):
        print(f"The max value from the {col} is: ", df_data[col].value_counts())


print(f"the following max value for Total bill is: ", df_data['sex'].value_counts())


print('------------------------------------------------------------------')

# Q7. Add a new column called 'tip_percentage'
#     Formula: (tip / total_bill) * 100
# What you learn: creating derived columns — very common in real work
# Hint: df['tip_percentage'] = ...
'''
create a new column and add the formula to get the data
'''

df_data['tip_percentage'] = (df_data['tip']/df_data['total_bill']) * 100
print(df_data.head())


print('------------------------------------------------------------------')
# Q8. What is the average tip percentage by gender?
# What you learn: groupby + mean on a custom column you created
# Hint: df.groupby('sex')['tip_percentage'].mean()

'''
here group by is used: to refer more about this topic, refer Panda_New_Topics.py

we will categories tip percentage with each category as well using loop
'''

df_groupby =  df_data.groupby('sex')['tip_percentage'].mean()
print(f"For each category, The average tip is: ", df_groupby)

for col in df_data.columns:
    if pd.api.types.is_string_dtype(df_data[col]):
        print(f"For category {col}, The average tip is: ", df_data.groupby(col)['tip_percentage'].mean())


# Q9. Which day of the week has the highest TOTAL tip collected?
# What you learn: groupby + sum + sort
# Hint: .groupby('day')['tip'].sum().sort_values(ascending=False)

# Q10. Filter only the rows where tip percentage is above 20%
#      How many such rows are there?
# What you learn: boolean filtering — most used pandas skill
# Hint: df[df['tip_percentage'] > 20]

# Q11. What is the average total bill for smokers vs non-smokers?
# What you learn: groupby on yes/no column
# Hint: df.groupby('smoker')['total_bill'].mean()

# Q12. On which day do smokers tip the most on average?
# What you learn: groupby on multiple columns
# Hint: df.groupby(['smoker', 'day'])['tip'].mean()

