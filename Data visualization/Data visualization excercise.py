#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

recent_grads=pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0])
print(recent_grads.head)
print(recent_grads.tail)
recent_grads.describe()


# In[6]:


recent_grads=recent_grads.dropna()


# In[7]:


recent_grads.plot(x='Sample_size',y='Median',kind='Scatter')


# In[8]:


recent_grads.plot(x='Sample_size',y='Unemployment_rate',kind='Scatter')


# In[9]:


recent_grads.plot(x='Full_time',y='Median',kind='Scatter')


# In[10]:


recent_grads.plot(x='ShareWomen',y='Unemployment_rate',kind='Scatter')


# In[11]:


recent_grads.plot(x='Men',y='Median',kind='Scatter')


# In[12]:


recent_grads.plot(x='Women',y='Median',kind='Scatter')


# In[29]:


cols=["Sample_size","Median","Employed","Full_time","ShareWomen",
      "Unemployment_rate","Men","Women"]

fig=plt.figure(figsize=(5,12))

for r in range (0,4):
    ax = fig.add_subplot(4,1,r+1)
    ax = recent_grads[cols[r]].plot(kind='hist',rot=30)


# In[31]:


cols=["Sample_size","Median","Employed","Full_time","ShareWomen",
      "Unemployment_rate","Men","Women"]

fig=plt.figure(figsize=(5,12))

for r in range (4,8):
    ax = fig.add_subplot(4,1,r-3)
    ax = recent_grads[cols[r]].plot(kind='hist',rot=30)


# In[32]:


from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))


# In[33]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[34]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[ ]:




