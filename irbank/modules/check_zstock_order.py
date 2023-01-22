#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-----------------------------------------------------------------------7:ここから一株当たり-----------------------------------------------------------------------------------------#

def check_zstock_order(zstock_list):
    result = all(float(zstock_list[i]) < float(zstock_list[i+1]) for i in range(len(zstock_list)-1))
    hitokabu_stock=[]
    if result:
        hitokabu_stock.append('OK')
    else:
        for i in range(len(zstock_list)-1):
            if float(zstock_list[i]) >= float(zstock_list[i+1]):
                hitokabu_stock.append(f'NOT (at index {i+1})')
    return hitokabu_stock

