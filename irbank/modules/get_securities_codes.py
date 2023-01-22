#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pickle
from functools import cache
from bs4 import BeautifulSoup
import requests 
import re
from time import sleep
import pandas as pd
import time
from tqdm import tqdm
import pickle
import itertools
import os.path
import random 
# 関数の実行時間を測るデコレータ
def tictoc(func):
    def _wrapper(*args, **keywargs):
        start_time = time.time()
        result = func(*args, **keywargs)
        print('time: {:.9f} [sec]'.format(time.time() - start_time))
        return result
    return _wrapper

@tictoc
@cache
def get_securities_codes(start_page, end_page):
    url='https://minkabu.jp/financial_item_ranking/dividend_yield?page={}'
    dd_list=[]
    for i in range(start_page, end_page+1):
        target_url=url.format(i)
        r=requests.get(target_url)
        sleep(random.uniform(3, 8))
        soup=BeautifulSoup(r.text,'html.parser')
        tab=soup.find('table',class_='md_table rnk_li')
        conts=tab.find_all('tr')
        del conts[0]

        for cont in conts:
            rank=cont.find('span',class_='ranking_no fsize_l').text
            code=cont.find('div',class_='md_sub').text
            name=cont.find('div',class_='fwb w90p').text
            y=cont.find('td',class_='tar cur vamd').text
            yeild= y.strip().replace('%', '')
            dic={
                'ランキング':rank,
                '証券コード':code,
                '企業名':name,
                '配当利回り':yeild,
            }
            
            if float(yeild) >= 3.75:
                dd_list.append(dic)
    securities_codes = [d['証券コード'] for d in dd_list]
    #csvに保存まだ更新はできず追加しかされない
    new_data=pd.DataFrame(dd_list)
    if os.path.exists('csv/20230122ranking.csv'):
                df=pd.read_csv('csv/20230122ranking.csv')
                df=pd.concat([df, new_data], ignore_index=True)
                
    else:
        df=new_data
    df.to_csv('csv/20230122ranking.csv',index=None,encoding='utf-8-sig')

    return securities_codes

