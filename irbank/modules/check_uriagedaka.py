#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#評価する関数
#--------------------------------------------------------------------- １:売上高----------------------------------------------------------------------------------------------------------------#

def check_uriagedaka(eval_sale_list):
    result = all(int(eval_sale_list[i]) < int(eval_sale_list[i+1]) for i in range(len(eval_sale_list)-1))
    uriagedaka_stock = []
    if result:
        uriagedaka_stock.append('OK')
    else:
        for i in range(len(eval_sale_list)-1):
            if int(eval_sale_list[i]) >= int(eval_sale_list[i+1]):
                uriagedaka_stock.append(f'NOT (at index {i+1})')
    return uriagedaka_stock

    

