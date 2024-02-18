#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[79]:


df = pd.read_csv('D:/DATA SCIENCE/Python/Python_Diwali_Sales_Analysis-main/Diwali.csv', encoding= 'unicode_escape')
df


# In[80]:


df.head()


# In[81]:


df.shape


# In[82]:


df.info()


# In[83]:


# drop function to delete columnsdf.
df.drop(['Status','unnamed1'],axis=1,inplace= True)


# In[84]:


df.isnull().sum()


# In[85]:


#drop nulll value
df.dropna(inplace=True)


# In[86]:


#change data type
df['Amount']= df['Amount'].astype('int') 


# In[87]:


df['Amount'].dtypes


# In[88]:


df.columns


# In[89]:


# rename column name
df.rename(columns={'Marital_Status':'Shadi'})


# In[90]:


df.describe()


# In[91]:


# EDA
#Gender


# In[92]:


ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[93]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y='Amount',data=sales_gen)


# fro above graph we can see most of the buyers are female and purchasing power of female are greater than men

# In[94]:


#Age


# In[95]:


ax = sns.countplot(data= df, x= 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[96]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount',data=sales_age)


# from the above graphs we can see most of the buyers are of age between 26-35 yrs

# In[97]:


df.head()


# In[76]:


#Marital status


# In[101]:


ax = sns.countplot(data=df, x = 'Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)


# In[104]:


sales_status = df.groupby(['Marital_Status', 'Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data= sales_status, x='Marital_Status',y='Amount',hue='Gender')


# for above graph we can most of the buyers are married women and they are highly purchasing power

# In[105]:


#occupation


# In[107]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data= df, x= 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[109]:


sales_occ = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending= False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data= sales_occ, x = 'Occupation', y ='Amount')


# from the above graph we can see that most of the buyers are working in IT, HEalthcare and Aviation sector
# 

# In[110]:


#product category


# In[116]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data= df, x = 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[114]:


sales_occ = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending= False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data= sales_occ, x = 'Product_Category', y ='Amount')


# from the above graph we can see that most of sold product are from food, clothings and electronics

# In[117]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data= df, x = 'State')
for bars in ax.containers:
    ax.bar_label(bars)


# In[122]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data= sales_state, x = 'State', y ='Amount')


# # Conclusion

# married women age group 26-35yrs from UP, maharashtra, karnataka working in IT, healthcare and Avaition are more likely buy 
# product from food, clothings and electronics category
