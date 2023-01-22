#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_yeild(eval_yeild_lists):
    result = all(int(eval_yeild_lists[i]) < int(eval_yeild_lists[i+1]) for i in range(len(eval_yeild_lists)-1))
    yeild_stock = []
    if result:
        yeild_stock.append('OK')
    else:
        for i in range(len(eval_yeild_lists)-1):
            if int(eval_yeild_lists[i]) >= int(eval_yeild_lists[i+1]):
                yeild_stock.append(f'NOT (at index {i+1})')
    return yeild_stock

