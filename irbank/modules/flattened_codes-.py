#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pickle
import itertools
from get_securities_codes import *
def get_flattened_codes(get_securities_codes, file_path):
    result = {}
    #1ページ目から取得なので値に0はいらない
    for page in range(1, 37):
        securities_codes = get_securities_codes(page, page)
        result[page] = securities_codes
        if os.path.exists(file_path):
         # ファイルから既存のデータを読み込む
            with open(file_path, 'rb') as f:
                existing_data = pickle.load(f)
            # 既存のデータを更新する
            existing_data.update(result)
            # ファイルに追加されたデータを保存する
            with open(file_path, 'wb') as f:
                pickle.dump(existing_data, f)
        else:
            with open(file_path, 'wb') as f:
                pickle.dump(result, f)

    #全部のリストをつなげる(このページで取得するものはflattened_codes=企業コードで終了)
    with open(file_path, 'rb') as f:
                existing_data = pickle.load(f)
    if existing_data[0] :
        del existing_data[0]
    else:
        pass
    #flatyeild_urls.pyとflatclosing_urls.pyで読み込まれる（使われる）
    flattened_codes = list(itertools.chain(*existing_data.values()))
    return flattened_codes

# In[ ]:




