#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
def get_yeild_urls(start_code, end_code,file_path):
    print(datetime.now().strftime("%H:%M:%S"))
    yeild_dict = {}
    for code in flattened_codes[start_code:end_code]:
        yeuld_url = get_yeild_curve(code)
        yeild_dict[code] = yeuld_url

    # 既存のpickleファイルがある場合
    if os.path.exists(file_path):
        # ファイルから既存のデータを読み込む
        with open(file_path, 'rb') as f:
            ye_data = pickle.load(f)
        # 既存のデータに新しいデータを追加
        ye_data.update(yeild_dict)
        # ファイルに追加されたデータを保存する
        with open(file_path, 'wb') as f:
            pickle.dump(ye_data, f)
    # 初めての保存の場合
    else:
        with open(file_path, 'wb') as f:
            pickle.dump(yeild_dict, f)
    with open(file_path, 'rb') as f:
            ye_data = pickle.load(f)
    flatyeild_urls = list(itertools.chain(ye_data.values()))
    print(datetime.now().strftime("%H:%M:%S"))
    return flatyeild_urls


# In[ ]:




