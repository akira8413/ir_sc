#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#--------------------------------------------------------------------------6:ここからCF ------------------------------------------------------------------------------------------#

def check_cflow_order(eval_cf_flow_list):
    result = all(int(eval_cf_flow_list[i]) < int(eval_cf_flow_list[i+1]) for i in range(len(eval_cf_flow_list)-1))
    cflow_stock=[]
    if result:
        cflow_stock.append('OK')
    else:
        for i in range(len(eval_cf_flow_list)-1):
            if int(eval_cf_flow_list[i]) >= int(eval_cf_flow_list[i+1]):
                cflow_stock.append(f'NOT (at index {i+1})')
    return cflow_stock

