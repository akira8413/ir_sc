#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------8:配当性向--------------------------------------------------------------------------------------------------------------#
def convert_return(return_figure: str) -> str:
    if '.' in return_figure:
        number_str = return_figure.split('%')[0]
        integer_part, decimal_part = number_str.split('.')
        integer_part = integer_part.zfill(2)
        decimal_part = decimal_part.zfill(2)
        return f"{integer_part}.{decimal_part}"
    else:
        integer_part = return_figure.split('%')[0]
        integer_part = integer_part.zfill(2)
        return f"{integer_part}.00"

    

