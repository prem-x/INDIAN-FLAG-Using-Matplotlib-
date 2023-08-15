#!/usr/bin/env python
# coding: utf-8

# # INDIAN FLAG MADE WTIH MATPLOTLIB !! 

# ###### -BY PREM AKKATANGERHAL 

# In[55]:


import matplotlib.pyplot as plt


# In[56]:


import numpy as np


# In[57]:


a = plt.Rectangle((0,1), height = 2, width =12, facecolor = 'green', edgecolor = 'grey')
b = plt.Rectangle((0,3), height = 2, width =12, facecolor = 'white', edgecolor = 'grey')
c = plt.Rectangle((0,5), height = 2, width =12, facecolor = '#FF9933', edgecolor = 'grey')
d = plt.Circle((6,4), 0.8, fill=False, linewidth =7, color ='#000088ff' )


# In[58]:


plt.subplots()


# In[ ]:





# In[59]:


q,w = plt.subplots()
p = plt.Polygon([(0,0), (2.5,5), (3,9), (1,6)])
w.add_patch(p)
plt.axis("scaled")
plt.show()


# In[60]:


j,k = plt.subplots()
for i in range(0,24):
   p = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
   q = 6 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
   r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
   s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
   t = 6 + radius * np.cos(np.pi*i/12)
   u = 4 + radius * np.sin(np.pi*i/12)
   k.add_patch(plt.Polygon([[6,4], [p,r], [t,u],[q,s]], fill=True, closed=True, color='#000088ff'))
plt.axis('equal')
plt.show()


# In[61]:


n, m = plt.subplots()
m.add_patch(a)
m.add_patch(b)
m.add_patch(c)
m.add_patch(d)
plt.plot(6,4, marker = 'o', markerfacecolor = '#000088ff', markersize = 8.5)

radius = 0.8
for i in range(0,24):
   p = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
   q = 6 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
   r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
   s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
   t = 6 + radius * np.cos(np.pi*i/12)
   u = 4 + radius * np.sin(np.pi*i/12)
   m.add_patch(plt.Polygon([[6,4], [p,r], [t,u],[q,s]], fill=True, closed=True, color='#000088ff'))
plt.axis('scaled')
plt.axis('off')
plt.show()


# In[ ]:





# In[ ]:




