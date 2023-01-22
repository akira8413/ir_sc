#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convert_yeild_figure(yeild_figure: str) -> int:
    #兆しかない時
    if '兆' in yeild_figure and '億' not in yeild_figure and '万' not in yeild_figure:
        hennkan = yeild_figure.replace('兆', '*10**12')
        return eval(hennkan)
    #億しかない時
    elif '億' in yeild_figure and '兆' not in yeild_figure and '万' not in yeild_figure:
        hennkan = yeild_figure.replace('億', '*10**8')
        return eval(hennkan)
    #万しかない時
    elif '万' in yeild_figure and '兆' not in yeild_figure and '万' not in yeild_figure:
        hennkan = yeild_figure.replace('万', '*10**4')
        return eval(hennkan)
    elif '-' in yeild_figure and '兆' not in yeild_figure and '億' not in yeild_figure and '万' not in yeild_figure:
        hennkan=yeild_figure.replace('-','0')
        return eval(hennkan)
    #兆と億の時
    elif'兆'in yeild_figure and '億' in yeild_figure:
        hennkan = yeild_figure.replace('兆', '*10**12+').replace('億','*10**8')
        return eval(hennkan)
    #億と万の時
    elif'億'in yeild_figure and '万' in yeild_figure:
        hennkan = yeild_figure.replace('億', '*10**8+').replace('万','*10**4')
        return eval(hennkan)
    
    else:
        hennkan = re.sub(r"(兆)|(億)|(万)", lambda x: "*10**12+" if x.group(1) else "*10**8" if x.group(2) else "*10**4", yeild_figure)
        return eval(hennkan)
    

