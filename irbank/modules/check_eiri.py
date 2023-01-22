#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------3:ここから営業利益率2023/01/05- -------------------------------------------------------------------------#     

def check_eiri(zop_list):
    zop_list = [float(x) for x in zop_list]
    resault = all(10 <= float(zop_list[i]) for i in range(len(zop_list)))
    eiri_stock = []
    if resault:
        eiri_stock.append('OK')
    else:
        for i in range(len(zop_list)):
            if 10 >= float(zop_list[i]):
                eiri_stock.append(f'NOT (at index {i})')
    return eiri_stock

