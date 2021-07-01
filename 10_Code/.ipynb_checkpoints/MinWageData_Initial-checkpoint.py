#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


#Unemployment Data + Size of Labor Force
unemp = pd.read_excel('../00_source_data/ststdsadata.xlsx',header=7)
unemp.columns = ['FIPS_Code','State','Year','Month','Civilian_Pop','Civilian_Labor_Force','Labor_Force_Pct','Employed_Total','Employed_Pct','Unemployed_Total','Unemployed_Rate']
unemp = unemp[unemp['Year'] > 2009]
unemp.head()
#Unemployed total / civilian labor force = unemployment rate


# In[9]:


#GDP by State
gdp = pd.read_csv('../00_source_data/SAGDP1__ALL_AREAS_1997_2019.csv')
#gdp = gdp[gdp['Description'] == 'Real GDP (millions of chained 2012 dollars)']
gdp_phrase = gdp.Description[0]
gdp = gdp[gdp.Description == gdp_phrase]
gdp = gdp[['GeoFIPS','GeoName','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']]
gdp = gdp.set_index('GeoName')
gdp = gdp.drop(columns=['GeoFIPS'])
gdp = gdp.reset_index()
gdp = gdp.melt(id_vars='GeoName', var_name='Year', value_name='gdp')
gdp.sample(10)


# In[10]:


#Population
pop = pd.read_excel('../00_source_Data/nst-est2019-01.xlsx',header=3)
pop.rename( columns={'Unnamed: 0':'State'}, inplace=True )
pop = pop[['State',2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]]
pop = pop.melt(id_vars='State', var_name='Year', value_name='Population')
pop['State'] = pop['State'].str.replace('.', '')
pop.sample(10)


# In[11]:


#Dump these three tables into '20_intermediate files'
unemp.to_csv('../20_intermediate_files/unemployment_table.csv')
gdp.to_csv('../20_intermediate_files/gdp_table.csv')
pop.to_csv('../20_intermediate_files/population_table.csv')


# In[ ]:




