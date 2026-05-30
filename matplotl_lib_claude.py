# ============================================================
#                    MATPLOTLIB IN PYTHON
# ============================================================
# Matplotlib is a third-party library for creating visualizations.
#
# TWO WAYS TO USE IT:
#   1. pyplot API  -- simpler, most common, use this 90% of the time
#   2. Object Oriented API -- more control, used for complex subplots
#
# We use pyplot API here.
# INSTALL: pip install matplotlib
# IMPORT:  import matplotlib.pyplot as plt
#
# TYPES OF ANALYSIS:
#   Univariate  -- one variable at a time (age, salary, dept)
#   Bivariate   -- relationship between two variables
#   Multivariate-- relationship between three or more variables
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd

# basic plot to understand how plt.plot() works:
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

# pairs each x with its y and plots those points connected by a line:
# (1,5), (2,6), (3,7), (4,8)
plt.plot(x, y)
plt.grid()      # adds grid lines to the graph
plt.show()      # renders and displays the graph in a separate window
# NOTE: plt.show() returns None -- no point printing it


# ============================================================
#                    COMMON PLOT PARAMETERS
# ============================================================
# These parameters work across most plot types:
#
#   color      -- color of the line or bar ('red', 'green', '#FF5733')
#   marker     -- dot/symbol at each data point ('o', 's', '^', '*')
#   linestyle  -- style of the line ('-', '--', ':', '-.')
#   linewidth  -- thickness of the line (1, 2, 3...)
#   label      -- name shown in legend
#   alpha      -- transparency (0.0 = invisible, 1.0 = solid)
#   bins       -- number of bars in a histogram
#   edgecolors -- border color of markers or bars
#
# After plotting, these functions add context:
#   plt.title('...')    -- title at top
#   plt.xlabel('...')   -- label for x axis
#   plt.ylabel('...')   -- label for y axis
#   plt.grid()          -- adds grid lines
#   plt.legend()        -- shows labels as a legend box
#   plt.show()          -- renders the final graph
# ============================================================


# ============================================================
#             UNIVARIATE ANALYSIS -- ONE VARIABLE
# ============================================================
# Focus on understanding ONE column at a time.
# Either numerical (salary, age) or categorical (dept, yes/no).
# ============================================================

data = {
    'Salary(In Lakhs)': [25000, 57000, 12000, 67000, 23400, 73000, 123000]
}
df_data = pd.DataFrame(data)


# ------------------------------------------------------------
# Univariate Numerical
# ------------------------------------------------------------

# 1. Line Plot
# ------------
# Shows trend or pattern of a single numerical variable.
# x axis = index (row number by default), y axis = value.
# Good for seeing how values rise and fall across records.

plt.plot(df_data['Salary(In Lakhs)'],
         color='red',
         marker='o',        # 'o' puts a circle dot at each actual data point
         linestyle='--',    # '--' makes a dashed line instead of solid
         linewidth=2)       # thickness of the line
plt.grid()
plt.show()


# 2. Histogram
# ------------
# Shows the DISTRIBUTION of a numerical variable.
# Divides the range of values into buckets (bins) and counts
# how many values fall into each bucket.
# Good for answering: where are most values concentrated?
#
# bins=5 means divide the salary range into 5 equal buckets.
# Each bar height = number of people with salary in that range.

plt.hist(df_data['Salary(In Lakhs)'], bins=5, color='green')
plt.xlabel('Salary')
plt.ylabel('Count')
plt.title('Salary Distribution')
plt.show()

# HOW bins WORKS:
# salary range is roughly 12000 to 123000
# bins=5 divides this into 5 equal ranges
# each bar shows how many salaries fall in that range
# fewer bins = wider bars, more general picture
# more bins = narrower bars, more detailed picture


# 3. Box Plot
# -----------
# Shows the SPREAD and OUTLIERS of a numerical variable.
# This is the one you said you didn't understand -- explained fully here.
#
# A box plot shows 5 things:
#
#   |          <- top whisker    = maximum value (excluding outliers)
#   +---------+
#   |         |  <- top of box  = Q3 (75th percentile)
#   |---------|  <- line inside = median (middle value, Q2)
#   |         |  <- bottom of box = Q1 (25th percentile)
#   +---------+
#   |          <- bottom whisker = minimum value (excluding outliers)
#   o           <- dots beyond whiskers = OUTLIERS
#
# Q1 = 25% of values are below this
# Q3 = 75% of values are below this
# IQR = Q3 - Q1 (the box height -- shows where middle 50% of data lives)
# Whiskers extend to 1.5 * IQR beyond Q1 and Q3
# Any value beyond whiskers is plotted as a dot = OUTLIER
#
# WHAT TO READ FROM IT:
# - Tall box = data is spread out
# - Short box = data is clustered tightly
# - Median line near top = most values are low, a few are very high
# - Dots = outliers that are unusually high or low

plt.boxplot(df_data['Salary(In Lakhs)'])
plt.title('Salary Box Plot')
plt.show()


# ------------------------------------------------------------
# Univariate Categorical
# ------------------------------------------------------------
# For columns with categories like department, yes/no, region.

df_data['Dept'] = ['HR', 'IT', 'IT', 'HR', 'PR', 'IT', 'PR']

# value_counts() -- counts how many times each category appears:
count = df_data['Dept'].value_counts()
print(count)
# IT    3
# HR    2
# PR    2


# 1. Pie Chart
# ------------
# Shows each category as a SLICE of a circle.
# Slice size = proportion of that category in the total.
# Good for showing "what percentage is each category".
#
# count        = the values (sizes of slices)
# labels       = category names shown on the chart
# autopct      = format for percentage shown inside each slice
#                '%1.1f' means 1 decimal place (e.g. 42.9%)
# explode      = pulls a slice out to highlight it
#                [0, 0.1, 0] means pull the 2nd slice out by 0.1
# plt.axis('equal') = makes the circle perfectly round not oval

plt.pie(count,
        labels=count.index,
        autopct='%1.1f%%',
        explode=[0, 0.1, 0])
plt.axis('equal')
plt.title('Department Distribution')
plt.show()


# 2. Bar Chart (Count Plot)
# -------------------------
# Shows each category as a BAR, height = count of that category.
# Good for comparing counts across categories.
#
# count.index = category names for x axis
# count       = heights of bars (the counts)

plt.bar(count.index, count, color=['green', 'black', 'red'])
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Employees per Department')
plt.show()


# ============================================================
#           BIVARIATE ANALYSIS -- TWO VARIABLES
# ============================================================
# Understand the RELATIONSHIP between two columns.
# Three combinations:
#   Numerical vs Numerical   -- scatter, line, bar
#   Numerical vs Categorical -- boxplot, pie, bar
# ============================================================

df_data['age'] = [27, 46, 23, 32, 67, 66, 45]


# ------------------------------------------------------------
# Bivariate -- Numerical vs Numerical
# ------------------------------------------------------------

# 1. Scatter Plot
# ---------------
# Each row becomes a DOT on the graph.
# x = one numerical column, y = another numerical column.
# Good for seeing if two variables are RELATED (correlated).
# Pattern of dots rising = positive correlation (older = higher salary)
# Pattern of dots falling = negative correlation
# Random dots = no clear relationship

plt.scatter(df_data['age'], df_data['Salary(In Lakhs)'], color='orange')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()


# 2. Line Plot (two variables)
# ----------------------------
# Shows the relationship as a connected line.
# PROBLEM: if data is not sorted by x axis, the line jumps randomly.
# SOLUTION: sort by the x axis column first before plotting.

sort_age = df_data.sort_values('age')   # sort by age first
plt.plot(sort_age['age'],
         sort_age['Salary(In Lakhs)'],
         color='red',
         marker='o',
         linewidth=2)
plt.grid()
plt.title('Age vs Salary (Sorted)')
plt.show()

# WITHOUT sorting: line connects rows in original order -- messy zigzag
# WITH sorting: line connects in age order -- smooth left-to-right trend


# 3. Bar Chart (two numerical)
# ----------------------------
# Each bar represents one record.
# x = age (or any category), height = salary.

plt.bar(sort_age['age'], sort_age['Salary(In Lakhs)'], color='red')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


# ------------------------------------------------------------
# Bivariate -- Numerical vs Categorical
# ------------------------------------------------------------
# Split numerical data by category and compare distributions.
# First filter salary for each department:

hr_sal = df_data[df_data['Dept'] == 'HR']['Salary(In Lakhs)']
it_sal = df_data[df_data['Dept'] == 'IT']['Salary(In Lakhs)']
pr_sal = df_data[df_data['Dept'] == 'PR']['Salary(In Lakhs)']


# 1. Box Plot (multiple categories)
# ----------------------------------
# Shows salary spread for EACH department side by side.
# Now you can compare: which dept has higher salaries?
# Which dept has more variation? Which has outliers?
# Same box plot rules apply -- but now one box per category.

plt.boxplot([hr_sal, it_sal, pr_sal], labels=['HR', 'IT', 'PR'])
plt.ylabel('Salary')
plt.title('Salary Distribution by Department')
plt.show()

# READ IT AS:
# taller box = more salary variation within that dept
# higher median line = generally higher salaries
# dots = outlier employees earning unusually high or low


# 2. Pie Chart (salary share per dept)
# -------------------------------------
# Shows what PERCENTAGE of total salary each dept takes.
# groupby() adds up all salaries per department first.
# shadow=True adds a shadow effect behind the pie.

salary_by_dept = df_data.groupby('Dept')['Salary(In Lakhs)'].sum()
print(salary_by_dept)

plt.pie(salary_by_dept,
        labels=salary_by_dept.index,
        autopct='%1.2f%%',
        shadow=True)
plt.axis('equal')
plt.title('Salary Share by Department')
plt.show()


# 3. Bar Chart (mean salary per dept)
# ------------------------------------
# Calculate mean salary for each department manually.
# Then plot each dept as a bar with height = mean salary.
# Good for comparing average performance across categories.

hr_mean = sum(hr_sal) / len(hr_sal)
it_mean = sum(it_sal) / len(it_sal)
pr_mean = sum(pr_sal) / len(pr_sal)

plt.bar(['HR', 'IT', 'PR'],
        [hr_mean, it_mean, pr_mean],
        color=['green', 'red', 'black'])
plt.ylabel('Mean Salary')
plt.title('Average Salary by Department')
plt.grid()
plt.show()


# ============================================================
#          MULTIVARIATE ANALYSIS -- 3+ VARIABLES
# ============================================================
# Visualize three or more variables in a single chart.
# Achieved by mapping the third variable to size or color.
# ============================================================

df_data['Experience'] = [3, 5, 1, 6, 8, 4, 5]


# 1. Bubble Plot
# --------------
# Like a scatter plot but adds a THIRD variable as bubble SIZE.
# x = age, y = salary, SIZE of bubble = experience.
# Larger bubble = more experience.
# Good for seeing three numerical variables at once.
#
# s = size of each bubble -- multiply by 10 to make visible
# edgecolors = border color of each bubble

plt.scatter(df_data['age'],
            df_data['Salary(In Lakhs)'],
            s=df_data['Experience'] * 100,  # size mapped to experience
            color='orange',
            edgecolors='black',
            alpha=0.7)                      # slight transparency so bubbles dont fully overlap
plt.title('Age vs Salary vs Experience (Bubble Size)')
plt.xlabel('Age')
plt.ylabel('Salary(In Lakhs)')
plt.show()

# READ IT AS:
# position on x = age, position on y = salary
# size of bubble = experience
# a big bubble high on the chart = experienced AND high salary


# 2. Scatter Plot with Color per Category
# ----------------------------------------
# x = age, y = salary, COLOR of dot = department.
# Adds a categorical third variable using color mapping.
#
# .map({'HR': 'yellow', ...}) converts dept names to colors
# c = color array, one color per row

dept_colors = df_data['Dept'].map({'HR': 'yellow', 'IT': 'black', 'PR': 'green'})

plt.scatter(df_data['age'],
            df_data['Salary(In Lakhs)'],
            c=dept_colors)
plt.title('Age vs Salary colored by Department')
plt.xlabel('Age')
plt.ylabel('Salary(In Lakhs)')
plt.show()


# 3. Scatter with Legend (correct way)
# --------------------------------------
# The above approach loses department labels in the legend.
# To get a proper legend, loop over each department separately
# and plot each group individually with a label.
# plt.legend() then picks up those labels automatically.

color_map = {'HR': 'yellow', 'IT': 'black', 'PR': 'green'}

for dept, color in color_map.items():      # .items() not .item() -- common typo
    df_dept = df_data[df_data['Dept'] == dept]
    plt.scatter(df_dept['age'],            # plot only THIS dept's data
                df_dept['Salary(In Lakhs)'],
                c=color,
                label=dept)                # label is used by legend()

plt.title('Age vs Salary by Department')
plt.xlabel('Age')
plt.ylabel('Salary(In Lakhs)')
plt.legend()    # now shows HR, IT, PR with their colors
plt.show()

# WHY LOOP INSTEAD OF ONE SCATTER:
# If you plot all rows at once with c=dept_colors, matplotlib
# does not know which color belongs to which department label.
# By plotting each department separately with its own label,
# matplotlib can build the legend correctly.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Analysis Type      Chart            Use When
#  ──────────────────────────────────────────────────────────────
#  Univariate Num     Line plot        See trend across records
#  Univariate Num     Histogram        See distribution of values
#  Univariate Num     Box plot         See spread and outliers
#  Univariate Cat     Pie chart        See category proportions
#  Univariate Cat     Bar chart        Compare category counts
#  Bivariate N-N      Scatter plot     See correlation between 2 nums
#  Bivariate N-N      Line plot        Trend between 2 nums (sort first)
#  Bivariate N-C      Box plot         Compare spread across categories
#  Bivariate N-C      Bar chart        Compare mean per category
#  Bivariate N-C      Pie chart        Compare total share per category
#  Multivariate       Bubble plot      3 numerical vars (size = 3rd)
#  Multivariate       Colored scatter  2 numerical + 1 categorical
#
#  Box Plot cheat sheet:
#  ──────────────────────────────────────────────────────────────
#  Top whisker    = max (within 1.5 * IQR)
#  Top of box     = Q3 (75th percentile)
#  Line in box    = median
#  Bottom of box  = Q1 (25th percentile)
#  Bottom whisker = min (within 1.5 * IQR)
#  Dots outside   = outliers
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Always call plt.show() at the end to render the graph
#  2. Sort data by x axis before line plot with two variables
#  3. Use plt.legend() only when labels are assigned in scatter/plot
#  4. Loop per category when you need a legend in scatter plot
#  5. color_map.items() not .item() -- common typo
#  6. autopct='%1.1f%%' -- double %% needed for literal % sign
#
# ============================================================