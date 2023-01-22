#!/usr/bin/env python
# coding: utf-8
import flattened_codes.py
closing_dict = {}
for code in flattened_codes[700:713]:
    new_url = get_closing_url(code)
    closing_dict[code] = new_url

# 既存のpickleファイルがある場合
    if os.path.exists('csv/closing_dict.pickle'):
        # ファイルから既存のデータを読み込む
        with open('csv/closing_dict.pickle', 'rb') as f:
            ex_data = pickle.load(f)s
        # 既存のデータに新しいデータを追加
        ex_data.update(closing_dict)
        # ファイルに追加されたデータを保存する
        with open('csv/closing_dict.pickle', 'wb') as f:
            pickle.dump(ex_data, f)
    # 初めての保存の場合
    else:
        with open('csv/closing_dict.pickle', 'wb') as f:
            pickle.dump(closing_dict, f)
