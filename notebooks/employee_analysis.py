#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## 1. Numpy Analysis
# ## 2. Pandas Data Analysis
# ## 3. Data Cleaning 
# ## 4. Department Analysis
# ## 5. Data Visualization 

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv("../data/employees.csv")

print("Employee Data:")
display(df.head())

print("Department Count:")
print(df["department"].value_counts())

print("Average Salary:")
print(df["salary"].mean())

print("IT Employees:")
display(df[df["department"]=="IT"])





# In[5]:


print("Employee Count:", len(df))

print("Average Salary by Department:")
print(df.groupby("department")["salary"].mean())

get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[6]:


df["salary"] = df["salary"].fillna(df["salary"].median())
df = df.drop_duplicates()
df["salary"] = df["salary"].astype(int)

print("Employee Count:", len(df))
print(df.groupby("department")["name"].count())


# In[ ]:




