#!/usr/bin/env python
# coding: utf-8

# In[2]:


## This notebook is about cleaning and exploring the data about smartphones

## The data can be found from Kaggle: 
# https://www.kaggle.com/datasets/informrohit1/smartphones-dataset?resource=download


# In[3]:


# Retrieving and opening the data. 

# Importing necessary libraries.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/vartihe/OneDrive - BDO Oy/Documents/archive (1)/smartphones_cleaned_v6.csv")


# In[4]:


# Checking what is in the data 

print(data.head())


# In[5]:


# The data shows different smartphones brands and their models. The columns 
# are information about the phones, and their capabilities.

# The points of interest are the pricing, rating, and operation system (os)


# In[6]:


# Check for cleaning needs

print(data.info())


# In[7]:


# Everything seems to be in order, all the numerical values are integers or 
# floats, and non-numerical values are objects or booleans.

# However, the price column shows values with no decimal points. Let's 
# check the info more clearly

print(data.describe())


# In[8]:


# The price column in showing odd values. For example, the minimum value is 3499, 
# when the actual value is 34.99$. Let's convert the value for more suitable form.

data['price'] = data['price'] / 100.0


# In[9]:


print(data.head())


# In[10]:


# Let's see the price distribution, and format the table for better reading.

plt.figure(figsize=(20, 6))
sns.histplot(data['price'], kde=True)


# In[11]:


# The histogram shows that there are most phones under the pricerange or 500$.

# Next, we bring the operating system and see, how the operating system are 
# affecting to the price.

plt.figure(figsize=(20, 6))
sns.histplot(data=data, x='price', hue='os')


# In[12]:


# The histogram shows that most of the androids are below 1000$, and the 
# ios are scattered on both sides, slightly leaning heavy over 1000$.


# In[13]:


# The price vs. rating correlation can be seen from scatterplot. 

plt.figure(figsize=(20, 6))
sns.scatterplot(x='price', y='rating', data=data)


# In[14]:


# Adding a regression line for visualization

plt.figure(figsize=(20, 6))
sns.regplot(x=data['price'], y=data['rating'])


# In[15]:


# The data has values that are not valuable information. We can see that 
# there are three phones over 2000$, and their rating is not premium, 
# therefore we can filter them out, and try again with altered data and grid. 

data_2=data[data['price'] <= 2000]

sns.lmplot(x='price', y='rating', data=data_2, height=6, aspect=1.5)


# In[16]:


# There is a positive correlation with higher prices and higher ratings.

# The average price(mean) can be grouped by the brand. 

avg_price = data.groupby('brand_name')['price'].mean().sort_values()
avg_price.plot(kind='bar', figsize=(16, 6))


# In[17]:


# The top five expensive brands are huawei, apple, leitz, royole, and vertu. 
# The least expensive are lyf, itel, letv, gionee, and micromax. 
# For Finnish point of view, nokia is in the middle. 


# In[18]:


# The heatmap can give correlations between each numerical aspects. 

corr = data.corr()
plt.figure(figsize=(20, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')


# In[19]:


# There are highest positive correlations for price with internal memory, and 
# processor speed. The highest negative correlation for the price is the 
# availability of extended memory and battery capacity. 

# The ratings are high for those phones that have high ram capacity, 
# and high height resolution. 


# In[20]:


### Key findings:

## Most of the phones are under the pricerange or 500$. Androids are below 
# 1000$, and the ios are scattered on both sides, slightly leaning heavy over 
# 1000$.

## There is a positive correlation with higher prices and higher ratings.

## The ratings tend to be higher for those phones that have high ram capacity, and 
# high height resolution.

## There are high positive correlations for price with internal memory, and processor 
# speed. That means, the higher memoty or speed, the higher the price. 

## Highest negative correlation is between extended memory available and processor 
# speed. That means, the more extended memory there is available, the less processor 
# speed the phones has.

