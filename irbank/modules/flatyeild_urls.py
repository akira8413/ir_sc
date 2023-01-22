#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2
#ここから配当推移ページ
import pickle
import os
from get_yeild_curve import *


yeild_dict = {}

for code in flattened_codes[110:140]:
    yeuld_url = get_yeild_curve(code)
    yeild_dict[code] = yeuld_url

# 既存のpickleファイルがある場合
    if os.path.exists('csv/yeild_dict.pickle'):
        # ファイルから既存のデータを読み込む
        with open('csv/yeild_dict.pickle', 'rb') as f:
            ye_data = pickle.load(f)
        # 既存のデータに新しいデータを追加
        ye_data.update(yeild_dict)
        # ファイルに追加されたデータを保存する
        with open('csv/yeild_dict.pickle', 'wb') as f:
            pickle.dump(ye_data, f)
    # 初めての保存の場合
    else:
        with open('csv/yeild_dict.pickle', 'wb') as f:
            pickle.dump(yeild_dict, f)


