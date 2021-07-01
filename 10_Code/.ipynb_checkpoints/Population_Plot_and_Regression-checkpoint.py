#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from plotnine import *
from scipy.stats import ttest_ind
import statsmodels.api as sm
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings('ignore')


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
        + ylab(str('Population') + ' \n(Adding 95% confidence interval)')
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


# In[3]:


df = pd.read_csv('../20_intermediate_files/final_dataset.csv')
df = df.drop('Unnamed: 0', axis=1)
df['treatment'] = pd.Categorical(df['treatment'])


# In[4]:


plot_df_treated = df[df['treatment'] == 1].copy()
plot_df_control = df[df['treatment'] == 0].copy()

# Min wages between treatment and control split in 2015.

policy_implementation_year = 2015
resp_variable = 'Population'
file_name = 'Population_vs_Year'
plot = diff_in_diff_plot(plot_df_treated, plot_df_control, policy_implementation_year, resp_variable, file_name)
plot


# In[5]:


# Pre-post Plot Function

def pre_post_plot(df_treatment, policy_implementation_year, resp_variable, file_name):
    df_treatment['standardized_year'] = df_treatment['Year'] - policy_implementation_year
    lower_lim = df_treatment['standardized_year'].min()
    upper_lim = df_treatment['standardized_year'].max()+1
    plot = (
    ggplot() +
    geom_smooth(df_treatment[df_treatment['standardized_year'] < 0], 
                aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm') + 
    geom_smooth(df_treatment[df_treatment['standardized_year'] >= 0], 
                aes(x='standardized_year', y=resp_variable, color='treatment'), method='lm')
    + geom_vline(xintercept = 0) 
    + xlab('Years before/after Policy Implementation Year: '+str(policy_implementation_year) 
    + '. \nRepresented as "0" on the x-axis.') 
    + ylab(str(resp_variable) + ' \n(Adding 95% confidence interval)')
    + scale_x_continuous(breaks=range(lower_lim,upper_lim,1))
    + labs(title=str("Pre Post Plot"))
    )
    # Save plot to images folder.
    ggsave(filename=str('../20_intermediate_files/images/pre_post_'+file_name),
           plot=plot,
           dpi=150,
           height=8,
           width=8,
           verbose = False)
    return plot


# In[6]:


# Min wages between treatment and control split in 2015.

plot_df_treated = df[df['treatment'] == 1].copy()
plot_df_control = df[df['treatment'] == 0].copy()

policy_implementation_year = 2015

resp_variable = 'Population'
file_name = 'Population_vs_Time'

plot = pre_post_plot(plot_df_treated, policy_implementation_year, resp_variable, file_name)
plot


# In[7]:


# Separate the dataset into pre-treated and post-treated subsets

pre = df[np.logical_and(df['Year'] >= 2010,df['Year'] <= 2014)]
pre['Post'] = 0

post = df[np.logical_and(df['Year'] >= 2016,df['Year'] <= 2019)]
post['Post'] = 1

# Recombine the subsets 

selected_df = pd.concat([pre, post])
selected_df.head()


# In[8]:


# Regress Population on the predictors and their interactions

model = smf.ols('Population ~ C(treatment) + C(Post) + C(treatment)*C(Post)', selected_df).fit()

fe_groups = selected_df.copy()

model.get_robustcov_results(cov_type='cluster', groups=fe_groups.State).summary()

