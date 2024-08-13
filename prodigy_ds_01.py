# -*- coding: utf-8 -*-
"""PRODIGY_DS_01

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UkuydSrlbTZU6X30CI8XCaBIFBofGdZ5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv('/content/Sleep_health_and_lifestyle_dataset.csv')

data

'''I) Data Preprocessing:
Purpose: Prepare the raw data for further analysis'''

'''1) Data Cleaning:
           Purpose: Remove or correct inaccurate, incomplete, or irrelevant data.'''

'''-Checking for null values'''
data.isnull().sum()

''' so as we can see there null values only in the Sleep Disorder column which is categorical data.
    A null value in this column means there is no Sleep Disorder.
    We will fill null values here with a more meaningful value.
    it will be 'No Sleep Disorder' .
'''
data['Sleep Disorder'].fillna('No Sleep Disorder',inplace=True)

''' now lets check for null values again'''
data.isnull().sum()

''' as we can see there are no null values now.'''

'''-Checking for duplicate values'''
data.duplicated().sum()

''' as we can see there are no duplicate values in the dataset.'''

'''-Checking for wrong data types'''
data.dtypes

''' as we can see there are no wrong data types in the dataset.'''

'''-Checking for wrong data format'''
data.info()

'''  we can see there are no wrong data format in the dataset.'''

''' now we can move to exploratory data analysis (EDA)'''

data.describe()

''' we can do data profiling here as well'''

!pip install ydata-profiling==4.6.0

from ydata_profiling import ProfileReport

profile = ProfileReport(data, title="Profiling Report")
profile.to_notebook_iframe()

''' you can download the profile report here.'''
profile.to_file("report.html")

''' now we can move to data visualization'''

'''To visualize the distribution of "Age" (a continuous variable)
in your dataset,
you can create a histogram.'''
import matplotlib.pyplot as plt

plt.hist(data['Age'], bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.show()

''' we can make it more visually appealing like this '''

plt.figure(figsize=(10, 6))  # Set the figure size for better visibility
# Pass only the 'Age' column to plt.hist
plt.hist(data['Age'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Distribution of Ages', fontsize=16, fontweight='bold')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(['Age Distribution'], loc='upper right', fontsize=12)

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data preparation (assuming data is already loaded into the 'data' DataFrame)
age_data = data['Age']

# Choose a color map for a gradient effect
colors = plt.cm.viridis(np.linspace(0, 1, 15))

# Create the histogram
plt.figure(figsize=(10, 6))  # Set the figure size for better visibility
n, bins, patches = plt.hist(age_data, bins=15, color='skyblue', edgecolor='black', alpha=0.7)

# Apply the gradient color to each bin
for i in range(len(patches)):
    patches[i].set_facecolor(colors[i])

# Add labels and title with improved font properties
plt.xlabel('Age', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='darkblue')
plt.title('Distribution of Ages', fontsize=18, fontweight='bold', color='darkgreen')

# Customize the grid for a modern look
plt.grid(True, linestyle='-.', alpha=0.5, color='gray')

# Add a legend with a better location and style
plt.legend(['Age Distribution'], loc='upper right', fontsize=12, frameon=True, shadow=True)

# Show the plot
plt.show()

'''To visualize the distribution of a categorical variable, such as "Gender",
 you can create a bar chart.'''
import seaborn as sns
sns.countplot(x='Gender', data=data)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Genders')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a color palette
palette = sns.color_palette("Set2")

# Create the count plot with enhanced visuals
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data, palette=palette, saturation=0.8)

# Customize labels and title with improved font properties
plt.xlabel('Gender', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Count', fontsize=14, fontweight='bold', color='darkblue')
plt.title('Distribution of Genders', fontsize=18, fontweight='bold', color='darkgreen')

# Add value labels on top of the bars
for p in plt.gca().patches:
    plt.gca().annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', fontsize=12, color='black', xytext=(0, 8),
                       textcoords='offset points')

# Display the plot
plt.show()

''' we can also see the distribution of a categorical variable
like gender using a pie chart'''
import matplotlib.pyplot as plt

gender_counts = data['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Genders')
plt.show()

import matplotlib.pyplot as plt

# Calculate the counts for each gender category
gender_counts = data['Gender'].value_counts()

# Choose a color palette for the pie chart
colors = ['#66b3ff', '#99ff99', '#ffcc99']  # Soft and visually appealing colors

# Create the pie chart with enhanced features
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90,
        colors=colors, shadow=True, explode=[0.05]*len(gender_counts), textprops={'fontsize': 14})

# Add a title with improved font properties
plt.title('Distribution of Genders', fontsize=18, fontweight='bold', color='darkblue')

# Draw a circle in the middle to make it a donut chart (optional, for a modern look)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Display the plot
plt.show()