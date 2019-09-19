#!/usr/bin/env python
# coding: utf-8

# In[105]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")


# In[106]:


#load dataset
raw_df = pd.read_csv('Madison_crash_2009_2019.csv')


# In[107]:


raw_df['LGTCOND']


# In[17]:


raw_df.ACCDLOC.unique()


# In[25]:


#Check null value
raw_df.isna().sum()['HWYCLASS']


# When we zoom in the figure, it is clearly that red dots cluster in intersection areas, especially intersection of highways. Also, highway entrance and exit are the places where car crash happened a lot. And lots of red dots cluster in madison downtown which may indicate a possitive relation between car accident and car/pedestrian flow.

# In[114]:


def FeatureGPS(feature,detail,raw_df):
    #array stored GPS info about specific feature
    recordLA = []
    recordLO = []
    #drop null data
    raw_df_dropna = raw_df.dropna(subset=['WISLR_LATDECDG', 'WISLR_LONDECDG',feature]).reset_index(drop = True)
    items = raw_df_dropna.shape[0]
    #iterate all rows of data
    for i in range(items):
        if (raw_df_dropna['LGTCOND'][i] == detail):
            #print raw_df['WISLR_LATDECDG'][i]
            recordLA.append(raw_df_dropna ['WISLR_LATDECDG'][i])
            recordLO.append(raw_df_dropna ['WISLR_LONDECDG'][i])
    return recordLA,recordLO


# In[118]:


# Import gmplot library.
from gmplot import *
new_df = raw_df.fillna({'LGTCOND':'DAY'})
Darklat,Darklon = FeatureGPS('LGTCOND','DARK',new_df)
DAWNlat,DAWNlon = FeatureGPS('LGTCOND','DAWN',new_df)
DAYlat,DAYlon = FeatureGPS('LGTCOND','DAY',new_df)
DUSKlat,DUSKlon = FeatureGPS('LGTCOND','DUSK',new_df)
LIGHTlat,LIGHTlon = FeatureGPS('LGTCOND','LIGHT',new_df)


#declare the center of the map, and how much we want the map zoomed in
gmap3 = gmplot.GoogleMapPlotter(43.073207, -89.397674, 13)
# Scatter map
gmap3.scatter( Darklat,Darklon, '#ff0000 ',size = 25, marker = False ) #RED
gmap3.scatter( DAWNlat,DAWNlon, '#FFd700 ',size = 5, marker = False ) #YELLOW
gmap3.scatter( DAYlat,DAYlon, '#0000ff ',size = 2, marker = False )  #BLUE
gmap3.scatter( DUSKlat,DUSKlon, '#800080 ',size = 5, marker = False )#PURPLE
gmap3.scatter( LIGHTlat,LIGHTlon, '#065535 ',size = 5, marker = False )#DARK GREEN
# Location where you want to save your file.
gmap3.apikey = "AIzaSyBxDbRXvpObLuZDic6a1mbRiIr-FTnXLew"

gmap3.draw( "C:\\Users\\Mark Ji\\Desktop\\map11.html" )

print len(DAYlat)


# In[ ]:





# In[ ]:




