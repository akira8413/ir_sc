#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------4:ここから自己資本利益率------------------------------------------------------------------------#


def check_zikosihon(zoption_list):
    oolist = [float(x) for x in zoption_list]
    result = all(40 <= float(oolist[i]) for i in range(len(oolist)))
    zikosihon_stock = []
    if result:
        zikosihon_stock.append('OK')
    else:
        for i in range(len(oolist)):
            if 40 >= float(oolist[i]):
                zikosihon_stock.append(f'NOT (at index {i})')
    return zikosihon_stock

