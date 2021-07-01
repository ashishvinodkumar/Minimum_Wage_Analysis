#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[2]:


#Dump these three tables into '20_intermediate files'
unemp = pd.read_csv('../20_intermediate_files/unemployment_table.csv')
unemp = unemp.drop('Unnamed: 0', axis=1)
gdp = pd.read_csv('../20_intermediate_files/gdp_table.csv')
gdp = gdp.drop('Unnamed: 0', axis=1)
pop = pd.read_csv('../20_intermediate_files/population_table.csv')
pop = pop.drop('Unnamed: 0', axis=1)


# In[3]:


pop_gdp = pd.merge(pop, gdp, how='inner', left_on = ['State', 'Year'], right_on = ['GeoName', 'Year'], validate='1:1', indicator=True)
pop_gdp = pop_gdp[['State', 'Year', 'Population', 'gdp', '_merge']]
pop_gdp = pop_gdp.rename(columns={"_merge": "pop_gdp_merge"})

pop_gdp['Year'] = pop_gdp['Year'].astype('str')
unemp['Year'] = unemp['Year'].astype('str')


# In[4]:


df = pd.merge(unemp, pop_gdp, left_on = ['State', 'Year'], right_on = ['State', 'Year'], how='inner', validate='m:1', indicator=True)
df = df.drop(['pop_gdp_merge', '_merge'], axis=1)


# In[5]:


df.head()


# In[6]:


df.to_csv('../20_intermediate_files/final_dataset.csv')


# In[ ]:




