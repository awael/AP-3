#!/usr/bin/env python
# coding: utf-8

# In[357]:


import math
import random
from operator import add
data = [
    [5.5,4.2],
    [5.1,3.8],
    [4.7,3.2],
    [5.9,3.2],
    [4.9,3.1],
    [6.7,3.1],
    [5,3],
    [6,3],
    [4.6,2.9],
    [6.2,2.8]
    ]


# In[358]:


w, h = 10, 10
r = [[0 for x in range(w)] for y in range(h)]
a = [[0 for x in range(w)] for y in range(h)]
s = [[0 for x in range(w)] for y in range(h)]
e = [[0 for x in range(w)] for y in range(h)]


# In[359]:


z = []
for i in range (10):
    for j in range (10):
        s[i][j] = -((data[i][0]-data[j][0])*(data[i][0]-data[j][0])+(data[i][1]-data[j][1])*(data[i][1]-data[j][1]));
        z.append(s[i][j])


# In[ ]:





# In[360]:


# Insert Self-Similarity here
for i in range (10):
    s[i][i] = -2.109502311
# -0.141421356 is the lowest similarity


# In[361]:


for iterations in range (2000):
    for i in range (10):
        for k in range (10):
            maximum = -99999
            for kk in range (k):
                if (a[i][kk]+s[i][kk] > maximum):
                       maximum = a[i][kk]+s[i][kk]
            for kk in range (k+1,10):
                if (s[i][kk] + a[i][kk] > maximum):
                    maximum = s[i][kk]+a[i][kk]
        
            r[i][k] =  (s[i][k] - maximum) + 0.9 * r[i][k]
#           learning rate added as it was too fast
    for i in range (10):
        for k in range (10):
            if (i==k):
                summ = 0
                for ii in range (i):
                    summ += max(0,r[ii][k])
                for ii in range (i+1,10):
                    summ += max(0,r[ii][k])
                a[i][k] = summ*(1-0.9) + 0.9*a[i][k]
            else:
                summ = 0
                for ii in range (min(i,k)):
                    summ += max(0,r[ii][k])
                for ii in range (min(i,k)+1,max(i,k)):
                    summ += max(0,r[ii][k])
                for ii in range (max(i,k)+1,10):
                    summ += max(0,r[ii][k])
                a[i][k] = (1-0.9)*min (0,r[k][k]+summ) + 0.9*a[i][k]


# In[362]:


final = []
for i in range (10):
    e[i][i] = r[i][i] + a[i][i]
    if (e[i][i]>0):
        final.append(i)
# exemplar Matrix


# In[363]:


idx = [0 for x in range(10)] 
for i in range (10):
    indexx = 0
    maxim = -99999
    for j in range (len(final)):
        c = final[j]
        if (s[i][c]>maxim):
            maxim = s[i][c]
            indexx = c
    idx[i] = indexx + 1
# Assign exemplars to points


# In[364]:


print(idx)

