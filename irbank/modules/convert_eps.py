#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convert_eps(eps_figure: str) -> int:
    number_str = eps_figure.split('円')[0]
    hennkan = number_str + '*100'
    return eval(hennkan)

