#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


raw_df = pd.read_csv('Madison_crash_2009_2019.csv')


# In[8]:


raw_df['ACCDDATE']


# In[15]:


raw_df['ACCDDATE'] = pd.to_datetime(raw_df['ACCDDATE'])
ACCDYEAR = [x.year for x in raw_df['ACCDDATE']]
ACCDMONTH = [x.month for x in raw_df['ACCDDATE']]
raw_df['ACCDYEAR'] = ACCDYEAR
raw_df['ACCDMONTH'] = ACCDMONTH
raw_df

