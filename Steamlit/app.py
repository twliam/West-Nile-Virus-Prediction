#!/usr/bin/env python
# coding: utf-8

# # Spray

# ## Import Libraries

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np
import time 
import plotly.express as px
from plotly.offline import iplot


# ## Import Dataset

# In[4]:


df_spray=pd.read_csv('./00-Datasets/spray_cleaned.csv')
df_train=pd.read_csv('./00-Datasets/train_cleaned.csv')


# ## Map 

# ### Spray Locations from 2011-2013

# In[8]:


MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
px.set_mapbox_access_token(MAPBOX_TOKEN)
fig = px.scatter_mapbox(df_spray, lat = 'latitude', lon  = 'longitude',animation_frame="date",size_max=15, zoom = 10)

fig.update_layout(title = 'Spray Locations from 2011-2013',
    autosize=False,
    width=500,
    height=700,mapbox_accesstoken=MAPBOX_TOKEN,mapbox_style="light")

fig.show()


# ### Traps Locations from 2007-2013

# In[7]:


MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
px.set_mapbox_access_token(MAPBOX_TOKEN)
fig_trap = px.scatter_mapbox(df_train, lat = 'latitude', lon  = 'longitude',animation_frame="date",size_max=15, zoom = 10)

fig_trap.update_layout(title = 'Traps Locations from 2007-2013',
    autosize=False,
    width=500,
    height=700,)

fig_trap.show()


# In[ ]:





# In[ ]:





# In[10]:


st.plotly_chart(fig, use_container_width=True)


# ### 

# In[ ]:





# In[ ]:





# In[ ]:




# In[ ]:




