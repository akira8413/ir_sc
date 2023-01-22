#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------8:配当性向--------------------------------------------------------------------------------------------------------------#



def check_zreturn_range(zreturn_list):
    int_zreturn_list = [float(x) for x in zreturn_list]
    result = all(30<int(int_zreturn_list[i]<50) for i in range(len(int_zreturn_list)))
    seikou_stock=[]
    if result:
        seikou_stock.append('OK')
    else:
        for i in range(len(int_zreturn_list)):
            if int(30>int_zreturn_list[i] or int_zreturn_list[i]>70):
                seikou_stock.append(f'NOT (at index {i})')
    return seikou_stock


