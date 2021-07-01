#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from plotnine import *


# In[2]:


# Diff in Diff Plot Function
def diff_in_diff_plot(df_treatment, df_control, policy_implementation_year, resp_variable, file_name):
    
    df_treatment['standardized_year'] = df_treatment['Year'] - policy_implementation_year
    df_control['standardized_year'] = df_control['Year'] - policy_implementation_year
    
    lower_lim = df_treatment['standardized_year'].min()
    upper_lim = df_treatment['standardized_year'].max()+1
    
    plot = (
        ggplot() +
        geom_smooth(df_treatment[df_treatment['standardized_year'] < 0], 
                    aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm') + 
        geom_smooth(df_treatment[df_treatment['standardized_year'] >= 0], 
                    aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm') + 

        geom_smooth(df_control[df_control['standardized_year'] < 0], 
                    aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm') + 
        geom_smooth(df_control[df_control['standardized_year'] >= 0], 
                    aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm')
        + geom_vline(xintercept = 0) 
        + xlab('Years before/after Policy Implementation Year: '+str(policy_implementation_year) 
        + '. \nRepresented as "0" on the x-axis.') 
        + ylab(str('Unemployment Rate') + ' \n(Adding 95% confidence interval)')
        + scale_x_continuous(breaks=range(lower_lim,upper_lim,1))
        + labs(title=str("Difference in Difference Plot "))

    )
    
    # Save plot to images folder.
    ggsave(filename=str('../20_intermediate_files/images/'+file_name),
           plot=plot,
           dpi=150,
           height=8,
           width=8,
           verbose = False)

    
    return plot


# ### Load dataframe and subset to 6 target states

# In[3]:


df = pd.read_csv('../20_intermediate_files/final_dataset.csv')
df = df.drop('Unnamed: 0', axis=1)
states = ['South Dakota', 'West Virginia', 'Nebraska', 'Iowa', 'Idaho', 'Kansas']
df = df[df['State'].isin(states)]


# ### Create treatment and control states

# In[4]:


# Treatment = South Dakota, West Virginia, Nebraska
# Control = Iowa, Idaho, Kansas
condition = (df['State'] == 'South Dakota') | (df['State'] == 'West Virginia') | (df['State'] == 'Nebraska')
df['treatment'] = 0
df.loc[condition, 'treatment'] = 1
df = df.reset_index(drop=True)
df['treatment'] = pd.Categorical(df['treatment']) 


# ### Plot UnemploymentRate vs Time

# In[5]:


plot_df_treated = df[df['treatment'] == 1].copy()
plot_df_control = df[df['treatment'] == 0].copy()

# Min wages between treatment and control split in 2015.
policy_implementation_year = 2015
resp_variable = 'Unemployed_Rate'
file_name = 'UnemploymentRate_vs_Time'
plot = diff_in_diff_plot(plot_df_treated, plot_df_control, policy_implementation_year, resp_variable, file_name)
plot


# In[ ]:





# In[ ]:




