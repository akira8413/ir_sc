#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------2:EPS-------------------------------------------------------------------------#
 

def check_eps(zeps_list):
    result = all(int(zeps_list[i]) < int(zeps_list[i+1]) for i in range(len(zeps_list)-1))
    eps_stock = []
    if result:
        eps_stock.append('OK')
    else:
        for i in range(len(zeps_list)-1):
            if int(zeps_list[i]) >= int(zeps_list[i+1]):
                eps_stock.append(f'NOT (at index {i+1})')
    return eps_stock
    

