'''
# ============================================================
# PANDAS + NUMPY + MATPLOTLIB DRILL QUESTIONS
# Datasets: tips, iris, titanic (seaborn built-in)
# ============================================================
# HOW TO USE:
# - Attempt each question on your own first
# - Only look at hints if truly stuck
# - Focus on the QUESTION, not the function
# ============================================================

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')


# ============================================================
# DATASET 1: TIPS
# Context: A restaurant recorded bills, tips, and customer info
# ============================================================

# ---------- EASY ----------

# Q1. How many rows and columns does the tips dataset have?
# What you learn: df.shape, understanding dataset size
# Hint: .shape

# Q2. What are the data types of each column?
# What you learn: spotting which columns are numeric vs categorical
# Hint: .dtypes

# Q3. Are there any missing values in the dataset?
# What you learn: always check this before any analysis
# Hint: .isnull().sum()

# Q4. What is the average tip amount?
# What you learn: .mean() on a column
# Hint: df['tip'].mean()

# Q5. What is the highest total bill ever recorded?
# What you learn: .max()

# Q6. How many male vs female customers are there?
# What you learn: .value_counts()
# Hint: df['sex'].value_counts()


# ---------- MEDIUM ----------

# Q7. Add a new column called 'tip_percentage'
#     Formula: (tip / total_bill) * 100
# What you learn: creating derived columns — very common in real work
# Hint: df['tip_percentage'] = ...

# Q8. What is the average tip percentage by gender?
# What you learn: groupby + mean on a custom column you created
# Hint: df.groupby('sex')['tip_percentage'].mean()

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


# ---------- HARD ----------

# Q13. Find the top 5 highest tipping customers (by tip percentage)
#      Show their total_bill, tip, tip_percentage, and day
# What you learn: sort + head + column selection

# Q14. What is the correlation between total_bill and tip?
#      What does this tell you?
# What you learn: numpy/pandas correlation, interpreting results
# Hint: np.corrcoef() or df[['total_bill','tip']].corr()

# Q15. Create a summary table showing for each day:
#      - Total bills collected
#      - Average tip
#      - Number of customers
#      - Average tip percentage
# What you learn: .agg() with multiple functions — very powerful
# Hint: df.groupby('day').agg({'total_bill':'sum', 'tip':'mean', ...})


# ---------- MATPLOTLIB (TIPS) ----------

# Q16. Plot a bar chart showing average tip by day
#      Label x-axis, y-axis, and give it a title
# What you learn: basic bar chart, axis labels — most common plot in real work

# Q17. Plot a scatter plot of total_bill vs tip
#      Color the dots differently for lunch vs dinner
# What you learn: scatter plot, using color to show a third variable

# Q18. Plot a histogram of tip_percentage
#      Add a vertical line showing the mean tip percentage
# What you learn: histogram + axvline — showing distribution with reference point


# ============================================================
# DATASET 2: IRIS
# Context: Measurements of 3 flower species (setosa, versicolor, virginica)
# ============================================================

# ---------- EASY ----------

# Q1. How many flowers of each species are in the dataset?
# What you learn: value_counts on a category column

# Q2. What is the min, max, and mean of petal_length across all flowers?
# What you learn: describe() or individual aggregations

# Q3. Which species has the largest average petal length?
# What you learn: groupby + mean + idxmax

# Q4. Are there any missing values?


# ---------- MEDIUM ----------

# Q5. For each species, find the average of ALL four measurements
#     (sepal_length, sepal_width, petal_length, petal_width)
# What you learn: groupby on multiple numeric columns at once

# Q6. Find all flowers where petal_length > 5 AND petal_width > 1.8
#     Which species do they mostly belong to?
# What you learn: multiple conditions in filtering (use & not 'and')

# Q7. Add a new column called 'petal_area' = petal_length * petal_width
#     Which species has the highest average petal area?
# What you learn: creating meaningful derived columns

# Q8. Using numpy, find the standard deviation of sepal_length for each species
# What you learn: numpy inside a pandas groupby operation
# Hint: df.groupby('species')['sepal_length'].apply(np.std)


# ---------- HARD ----------

# Q9. Normalize the petal_length column between 0 and 1
#     Formula: (value - min) / (max - min)
# What you learn: numpy vectorized operations, normalization — used in ML prep

# Q10. Find which two species are most similar based on average measurements
#      (compare their averages and find the smallest difference)
# What you learn: groupby + comparing results programmatically

# Q11. Create a correlation matrix of all four numeric columns
#      Which two measurements are most strongly correlated?
# What you learn: .corr() on a DataFrame — important analytical skill


# ---------- MATPLOTLIB (IRIS) ----------

# Q12. Plot a scatter plot of sepal_length vs petal_length
#      Use different colors for each species
#      Add a legend
# What you learn: scatter with hue-like coloring manually

# Q13. Plot 4 histograms (one per measurement) in a 2x2 grid
# What you learn: subplots — essential for presenting multiple charts
# Hint: fig, axes = plt.subplots(2, 2)

# Q14. Plot a bar chart comparing average petal_area across species
# What you learn: combining a derived column with visualization


# ============================================================
# DATASET 3: TITANIC
# Context: Passenger survival data from the Titanic disaster
# ============================================================

# ---------- EASY ----------

# Q1. What percentage of passengers survived?
# What you learn: mean on a 0/1 column gives percentage directly

# Q2. How many passengers were in each class (1st, 2nd, 3rd)?
# What you learn: value_counts on pclass

# Q3. What was the average age of passengers?
#     Note: age has missing values — handle them
# What you learn: mean ignores NaN by default, but good to be aware

# Q4. How many missing values are in each column?
#     Which column has the most missing data?
# What you learn: isnull().sum().sort_values()


# ---------- MEDIUM ----------

# Q5. What is the survival rate by gender?
#     Who survived more — male or female?
# What you learn: groupby + mean on binary column

# Q6. What is the survival rate by passenger class?
# What you learn: groupby, understanding class-based patterns

# Q7. Fill missing age values with the median age
#     Then verify no missing values remain in that column
# What you learn: fillna() — most common data cleaning operation

# Q8. What is the average fare paid by survivors vs non-survivors?
# What you learn: groupby on survived column

# Q9. Create a new column 'age_group':
#     'child' if age < 18, 'adult' if age >= 18
# What you learn: np.where() — very powerful for conditional column creation
# Hint: np.where(condition, 'child', 'adult')


# ---------- HARD ----------

# Q10. What is the survival rate by age_group AND gender combined?
#      Which group had the best survival rate?
# What you learn: multi-column groupby, reading complex results

# Q11. Find the top 3 most expensive fares paid
#      Show the passenger's name (if available), class, survival status
# What you learn: sort + head + column selection

# Q12. Among passengers who did NOT survive:
#      What was the most common class and gender combination?
# What you learn: filtering + groupby + value_counts chained together

# Q13. Calculate the survival rate for each class+gender combination
#      Present it as a clean pivot table
# What you learn: pivot_table() — one of the most powerful pandas tools
# Hint: df.pivot_table(values='survived', index='pclass', columns='sex', aggfunc='mean')


# ---------- MATPLOTLIB (TITANIC) ----------

# Q14. Plot a bar chart showing survival rate by passenger class
# What you learn: visualizing grouped results

# Q15. Plot side-by-side bars showing survival rate by class AND gender
# What you learn: grouped bar charts — common in business reporting

# Q16. Plot a histogram of passenger ages
#      Use different colors for survived vs not survived (overlay)
# What you learn: overlapping histograms, alpha transparency
# Hint: plt.hist(..., alpha=0.5)

# Q17. Create a 1x3 subplot showing survival rate by:
#      - Passenger class
#      - Gender
#      - Age group
# What you learn: subplots with real analytical content


# ============================================================
# FINAL CHALLENGE — combine all three datasets' skills
# ============================================================

# CHALLENGE 1 (Tips):
# Find the single best "type" of customer for the restaurant
# Define "best" yourself — highest tipper? most frequent? biggest bill?
# Support your answer with numbers AND one chart

# CHALLENGE 2 (Iris):
# Without using any ML library — using only pandas/numpy —
# can you identify which species a flower belongs to
# if you know its petal_length and petal_width?
# Build a simple rule using the averages you calculated

# CHALLENGE 3 (Titanic):
# Build a survival profile:
# "What kind of passenger had the best chance of survival?"
# Answer using groupby, filtering, and at least 2 charts
'''