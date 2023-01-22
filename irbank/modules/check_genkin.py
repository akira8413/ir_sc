#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------5:ここから現金------------------------------------------------------------------------------------------#


def check_genkin(eval_cash_list):
    result = all(int(eval_cash_list[i]) < int(eval_cash_list[i+1]) for i in range(len(eval_cash_list)-1))
    genkin_stock = []
    if result:
        genkin_stock.append('OK')
    else:
        for i in range(len(eval_cash_list)-1):
            if int(eval_cash_list[i]) >= int(eval_cash_list[i+1]):
                genkin_stock.append(f'NOT (at index {i+1})')
    return genkin_stock

