#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-----------------------------------------------------------------------7:ここから一株当たり-----------------------------------------------------------------------------------------#

def convert_stock_figure(stock_figure: str) -> int:
    if '.' in stock_figure and '*' not in stock_figure :
        number_str = stock_figure.split('円')[0]
        integer_part, decimal_part = number_str.split('.')
        integer_part = integer_part.zfill(2)
        decimal_part = decimal_part.zfill(2)
        return f"{integer_part}.{decimal_part}"
    elif '*' in stock_figure and '.' not in stock_figure :
        kn = stock_figure.split('*')[1]
        number_str1 = kn .split('円')[0]
        integer_part1 = number_str1.zfill(2)
        return f"{integer_part1}.00"
    
    elif'*'in stock_figure and '.' in stock_figure:
        kn = stock_figure.split('*')[1]
        number_str = kn.split('円')[0]
        integer_part, decimal_part = number_str.split('.')
        integer_part = integer_part.zfill(2)
        decimal_part = decimal_part.zfill(2)
        return f"{integer_part}.{decimal_part}"
    else:
        number_str = stock_figure.split('円')[0]
        integer_part = number_str.zfill(2)
        return f"{integer_part}.00"
    

