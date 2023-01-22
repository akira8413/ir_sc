#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-------------------------------------------------------------------------4:ここから自己資本利益率------------------------------------------------------------------------#
def floatparcent_hennkan(s):
    if '.' in s:
        number_str = s.split('%')[0]  # '15.65' のような文字列を取得
        integer_part, decimal_part = number_str.split('.')  # '15' と '65' のような文字列を取得
        integer_part = integer_part.zfill(2)  # 整数部を 0 で埋める
        decimal_part = decimal_part.zfill(2)  # 小数部を 0 で埋める
        hennkan_result = f"{integer_part}.{decimal_part}"  # 埋めた数値を結合
        return hennkan_result

    else:
        # 整数部と小数部が分離されていない場合
        integer_part = s.split('%')[0]  # '86' のような文字列を取得
        integer_part = integer_part.zfill(2)  # 整数部を 0 で埋める
        hennkan_result = f"{integer_part}.00"
        return hennkan_result
    

