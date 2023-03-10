#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data from online datasets
url1 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
url2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)

# Set the style of the plot
plt.style.use('ggplot')

# Plot the first line
plt.plot(df1['sepal_length'], label='Sepal Length')

# Plot the second line
plt.plot(df1['sepal_width'], label='Sepal Width')

# Plot the third line
plt.plot(df2['total_bill'], label='Total Bill')

# Set the x and y labels
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Set the title of the plot
plt.title('Multiple Line Plot with Labels and Legend')

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd

# Load data from online dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
df = pd.read_csv(url)

# Create two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

# Plot the first graph (scatter plot)
ax1.scatter(df['total_bill'], df['tip'], alpha=0.5, label='Data Points')
ax1.plot([0, 60], [0, 12], 'r--', label='Line of Best Fit')
ax1.set_xlabel('Total Bill')
ax1.set_ylabel('Tip Amount')
ax1.set_title('Scatter Plot of Tips')
ax1.legend()

# Plot the second graph (histogram)
ax2.hist(df['total_bill'], bins=20, alpha=0.5, label='Total Bill')
ax2.hist(df['tip'], bins=20, alpha=0.5, label='Tip Amount')
ax2.set_xlabel('Value')
ax2.set_ylabel('Frequency')
ax2.set_title('Histogram of Total Bill and Tip Amount')
ax2.legend()

# Adjust the layout of the subplots
fig.tight_layout()

# Show the plot
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd

# Load data from online dataset
url = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv'
df = pd.read_csv(url)

# Select data for countries of interest
countries = ['United States', 'China', 'India', 'Brazil', 'Mexico']
df = df[df['Country Name'].isin(countries)]

# Pivot data to create separate columns for each country
df = df.pivot(index='Year', columns='Country Name', values='Value')

# Plot the data
df.plot.line()
plt.title('Population of Selected Countries')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()

# Show the plot
plt.show()


# In[ ]:




