#!/usr/bin/env python
# coding: utf-8
import os
import pickle
importitertools
from get_securities_codes import get_securities_codes
result = {}
#1ページ目から取得なので値に0はいらない
for page in range(1, 2):
    securities_codes = get_securities_codes(page, page)
    result[page] = securities_codes
    if os.path.exists('csv/securities_codes.pickle'):
     # ファイルから既存のデータを読み込む
        with open('csv/securities_codes.pickle', 'rb') as f:
            existing_data = pickle.load(f)
        # 既存のデータを更新する
        existing_data.update(result)
        # ファイルに追加されたデータを保存する
        with open('csv/securities_codes.pickle', 'wb') as f:
            pickle.dump(existing_data, f)
    else:
        with open('csv/securities_codes.pickle', 'wb') as f:
            pickle.dump(result, f)

#全部のリストをつなげる(このページで取得するものはflattened_codes=企業コードで終了)
with open('pickle/securities_codes.pickle', 'rb') as f:
            existing_data = pickle.load(f)
if existing_data[0] :
    del existing_data[0]
else:
    pass
#flatyeild_urls.pyとflatclosing_urls.pyで読み込まれる（使われる）
flattened_codes = list(itertools.chain(*existing_data.values()))

