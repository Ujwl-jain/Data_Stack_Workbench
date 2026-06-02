'''
MATPLOTLIB

2 ways to use the matplot lib
1st pyplot API, Simpler and most common - use import matplotlib.pyplot as plt
2nd Using object oriented API, 


'''
import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4]
y = [5,6,7,8]

'''
it plots like this: 
(1,5), (2,6), (3,7), (4,8), on a graph.

'''
plt.plot(x,y)

# provide grids on the graph
plt.grid()
# shows the graph on a seperate window of a data set - plt.show() is a function
print(plt.show()) 

'''
pyplot API

import matplotlib.pyplot as plt

at what time which visual yo need to use according to the data set lets learn univariate analysis
'''

# UNIVARIATED ANALYSYS
'''
Focus on 1 variable at a time like age, weight , height, or a category like yes or no
'''

# ------------
# Univariated - Numerical
data = {
    'Salary(In Lakhs)' : [25000,57000,12000,67000,23400,73000,123000]
}

df_data = pd.DataFrame(data)
print(df_data)

# visualise the above dataframe

# 1. Line plot - we already seen, but now in detail

'''
plt.plot(df_data['Salary(In Lakhs)'], color = 'red', marker = 'o', linestyle = '--', linewidth = '2')

df_data['Salary(In Lakhs)'] - dataframe with the particular column name
color - allows you to set a specific color
linestyle - allows you to change the line style of a graph like stright line or dash line or dot line
marker - will highlight and show the point where the actual value is present on the graph
linewidth - gives the width to the line in the graph
'''
plt.plot(df_data['Salary(In Lakhs)'], color = 'red', marker = 'o', linestyle = '--', linewidth ='2')
plt.grid()
plt.show()

# 2. Histogram
'''

'''
plt.hist(df_data['Salary(In Lakhs)'], bins = 5, color = 'green')
plt.show()

# 3. Box Plot - samajh nhi aaya

plt.boxplot(df_data['Salary(In Lakhs)']) 
plt.show()

# ----------------
# Univariated - Categorical Column

# adding another column to categorise the columns 
df_data['Dept'] = ['HR', 'IT', 'IT', 'HR', 'PR', 'IT', 'PR']
print(df_data.head(2))

# 1. Pie chart
'''
count variable is needed for this chart,

lables = count.index will show the no. of counts for a particular category
explode will provide you to highlight a particular category
autopct will provide the percentage for the value
axis will make the circle equally 
'''
count = df_data['Dept'].value_counts()
print(count)

plt.pie(count, labels = count.index, autopct = '%1.1F', explode = [0,0.1,0])
plt.axis('equal')
plt.show()

# 2. countplot
'''
count  variable categories into a Bar graph
'''
plt.bar(count.index, count, color = ['green', 'black', 'red'])
plt.show()

# -----------
# Bivariate - numerical - numerical
'''
analsys between 2 different column, previous one was analsys of 1 particualr column whether it is categoricl or numercial
'''
df_data['age'] = [27,46,23,32,67,66,45]
print(df_data.head())

# 1. Scater plot
'''

'''
plt.scatter(df_data['age'], df_data['Salary(In Lakhs)'], color = 'orange')
plt.show()

# 2. Line plot
'''
Since using two values together on line plot makes it messier, it is cause of a certain column not sorted which makes the data randomly pointed
so we need to sort the certain column to make it pretier
'''
sort_age = df_data.sort_values('age')
plt.plot(sort_age['age'], sort_age['Salary(In Lakhs)'], color = 'red', marker = 'o', linewidth ='2')
plt.grid()
plt.show()

# 3. bar chart

plt.bar(sort_age['age'], sort_age['Salary(In Lakhs)'], color = 'red')
# plt.grid()
plt.show()

# -------------
# Bivariate - Numerical and categorical

'''

'''

hr_sal = df_data[df_data['Dept'] == 'HR']['Salary(In Lakhs)']
it_sal = df_data[df_data['Dept'] == 'IT']['Salary(In Lakhs)']
pr_sal = df_data[df_data['Dept'] == 'PR']['Salary(In Lakhs)']

# 1. Boxplot - samaj nhi aaya

plt.boxplot([hr_sal,it_sal,pr_sal], label=['HR','IT','PR'])
plt.show()

# 2. Pie Chart

'''

'''
salary_by_dept = df_data.groupby('Dept')['Salary(In Lakhs)'].sum()
print(salary_by_dept)

plt.pie(salary_by_dept, labels = salary_by_dept.index, autopct='%1.2f', shadow=True)
plt.axis('equal')
plt.show()

# 3. Bar plot
'''

'''
hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
pr_mean = sum(pr_sal)/len(pr_sal)


plt.bar(['HR','IT','PR'], [hr_mean,it_mean,pr_mean], color = ['green','red','black'])
plt.grid()
plt.show()


# -----------------
# Multivariant - using multiple numarical columns

df_data['Experience'] = [3,5,1,6,8,4,5]
print(df_data)

# 1. bubble plot - its like scatter plot
'''

'''
plt.scatter(df_data['age'],df_data['Salary(In Lakhs)'], s = df_data['Experience']*10, color = 'orange', edgecolors='black')
plt.title('Age vs Salary vs Experience')
plt.xlabel('Age')
plt.ylabel('Salary(In Lakhs)')
plt.show()

# 2. Scatterplot - using multivarient(2 numerical and 1 categorical)
# plt.scatter(df_data['age'],df_data['Salary(In Lakhs)'], c = df_data['Dept'].map({'HR' : 'yellow', 'IT' : 'black', 'PR': 'green'}))
# plt.title('Age vs Salary vs Experience')
# plt.xlabel('Age')
# plt.ylabel('Salary(In Lakhs)')
# plt.legend()
# plt.show()

'''
way of creating a legend for 2 numericaal and 1 categorical, multivarient -

'working couldnot understand'
'''
color = {'HR' : 'yellow', 'IT' : 'black', 'PR': 'green'}

# for dept,color in color.item():
#     df_dept = df_data[df_data['Dept'] == dept]
#     plt.scatter(df_data['age'],df_data['Salary(In Lakhs)'], c = color, label =dept)  


# Object oriented API
'''
WE CAN HAVE MULTPLE PLOTS AND SUBPLOTS IN SINGLE FIGURE

First we need to create a figure

meaning = (1,3) 1 is no of plot in which there will be 3 subplots
'''

fig, axs = plt.subplots(1,3, figsize = (15,5))

# lineplot
axs[0].plot(sort_age['age'], df_data['Salary(In Lakhs)'], color = 'red', marker = 'o', linewidth = '2')
axs[0].grid()
axs[0].set_title('line plot')

# histogram
axs[1].hist(df_data['Salary(In Lakhs)'],bins = 5, color = 'red')
axs[1].set_title('Histogram')
axs[1].set_xlabel('Salary')

# boxplot 
axs[2].boxplot(df_data['Salary(In Lakhs)'])
axs[2].set_title('boxplot')
axs[2].set_xlabel('Salary')

plt.show()

# to save the graphs and figure
plt.savefig('Name.jpg')
# or
plt.savefig(f'folderpath/Name.jpg')

# Multiple plot

# 3d plot

'''
End of these topics for matplotlib
'''
