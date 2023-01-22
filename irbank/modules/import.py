#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('run', "-i 'modules/get_securities_codes.py'")


# In[4]:


with open('csv/securities_codes.pickle', 'rb') as f:
            existing_data = pickle.load(f)
flattened_codes = list(itertools.chain(*existing_data.values()))
print(len(flattened_codes))


# In[50]:


#ここからclosing_dict=
import pickle
closing_dict = {}
for code in flattened_codes[30:50]:
    new_url = get_closing_url(code)
    closing_dict[code] = new_url

# 既存のpickleファイルがある場合
    if os.path.exists('irbank/csv/closing_dict.pickle'):
        # ファイルから既存のデータを読み込む
        with open('irbank/csv/closing_dict.pickle', 'rb') as f:
            ex_data = pickle.load(f)
        # 既存のデータに新しいデータを追加
        ex_data.update(closing_dict)
        # ファイルに追加されたデータを保存する
        with open('irbank/csv/closing_dict.pickle', 'wb') as f:
            pickle.dump(ex_data, f)
    # 初めての保存の場合
    else:
        with open('irbank/csv/closing_dict.pickle', 'wb') as f:
            pickle.dump(closing_dict, f)
            
            


# In[6]:


#全部のリストをつなげる(このページで取得するものはflatclosing_urls=決算ページのhrefで終了)
with open('csv/closing_dict.pickle', 'rb') as f:
            ex_data = pickle.load(f)
flatclosing_urls = list(itertools.chain(ex_data.values()))


# In[7]:


print(flattened_codes[0])
print(flatclosing_urls[0])


# In[ ]:


#余分なdataを削除
del existing_data[38]


# In[143]:


#辞書型のpickleにindexをつけてリストに
for i,key in enumerate(existing_data):
    print(i,key, existing_data[key])


# In[1]:


#全部のリストをつなげる
import itertools

flattened_codes = list(itertools.chain(*existing_data.values()))
print(len(flattened_codes))


# In[5]:


import time

# 関数の実行時間を測るデコレータ
def tictoc(func):
    def _wrapper(*args, **keywargs):
        start_time = time.time()
        result = func(*args, **keywargs)
        print('time: {:.9f} [sec]'.format(time.time() - start_time))
        return result
    return _wrapper


# In[ ]:





# In[ ]:


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


# In[335]:


with open('irbank/csv/securities_codes.pickle','rb') as f:
    securities_codes=pickle.load(f)


# In[78]:


def convert_eps(eps_figure: str) -> int:
    number_str = eps_figure.split('円')[0]
    hennkan = number_str + '*100'
    return eval(hennkan)


# In[77]:


def convert_sales(*args):
    eval_list = []
    for arg in args:
        eval_arg = []
        for value in arg:
            # 兆しかない時
            if '兆' in value and '億' not in value and '万' not in value:
                hennkan = value.replace('兆', '*10**12')
                eval_arg.append(eval(hennkan))
        eval_list.append(eval_arg)
    return eval_list


# In[369]:




def get_securities_codes(start_page, end_page):
    url='https://minkabu.jp/financial_item_ranking/dividend_yield?page={}'
    dd_list=[]
    for i in range(start_page, end_page+1):
        target_url=url.format(i)
        r=requests.get(target_url)
        sleep(5)
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
    return securities_codes





def float_hennkan(s):
    # *だけの時
    if '*' in s:
        s = s.split('円')[0]  # '15.65' のような文字列を取得
        s = s.replace('*', '')  # * を削除
        if '.'in s:
            integer_part, decimal_part =s.split('.')  # '15' と '65' のような文字列を取得
            integer_part = integer_part.zfill(2)  # 整数部を 0 で埋める
            decimal_part = decimal_part.zfill(2)  # 小数部を 0 で埋める
            hennkan_result= f"{integer_part}.{decimal_part}"  # 埋めた数値を結合
        return hennkan_result
    #小数点の時
    elif '.' in s :
        number_str = s.split('円')[0]  # '15.65' のような文字列を取得
        integer_part, decimal_part = number_str.split('.')  # '15' と '65' のような文字列を取得
        integer_part = integer_part.zfill(2)  # 整数部を 0 で埋める
        decimal_part = decimal_part.zfill(2)  # 小数部を 0 で埋める
        hennkan_result = f"{integer_part}.{decimal_part}"  # 埋めた数値を結合
        return hennkan_result
      

    else:
        # 整数部と小数部が分離されていない場合
        number_str = s.split('円')[0]  # '86' のような文字列を取得
        integer_part = number_str.zfill(2)  # 整数部を 0 で埋める
        hennkan_result = f"{integer_part}.00"
        return hennkan_result
    

#     if '.' in s:
#         number_str1 = kn .split('円')[0]  # '86' のような文字列を取得
#         integer_part1 = number_str1.zfill(2)  # 整数部を 0 で埋める
#         hennkan_result = f"{integer_part1}.00"
#         return hennkan_result
#     *だけの時
#     elif '*' in s:
#         kn = s.split('*')[1]
#         number_str1 = kn .split('円')[0]  # '86' のような文字列を取得
#         integer_part1 = number_str1.zfill(2)  # 整数部を 0 で埋める
#         hennkan_result = f"{integer_part1}.00"
#         return hennkan_result



def convert_sales_figure(sales_figure: str) -> int:
    #兆しかない時
    if '兆' in sales_figure and '億' not in sales_figure and '万' not in sales_figure:
        hennkan = sales_figure.replace('兆', '*10**12')
        return eval(hennkan)
    #億しかない時
    elif '億' in sales_figure and '兆' not in sales_figure and '万' not in sales_figure:
        hennkan = sales_figure.replace('億', '*10**8')
        return eval(hennkan)
    #万しかない時
    elif '万' in sales_figure and '兆' not in sales_figure and '万' not in sales_figure:
        hennkan = sales_figure.replace('万', '*10**4')
        return eval(hennkan)
    #兆と億の時
    elif'兆'in sales_figure and '億' in sales_figure:
        hennkan = sales_figure.replace('兆', '*10**12+').replace('億','*10**8')
        return eval(hennkan)
    #億と万の時
    elif'億'in sales_figure and '万' in sales_figure:
        hennkan = sales_figure.replace('億', '*10**8+').replace('万','*10**4')
        return eval(hennkan)
    else:
        hennkan = re.sub(r"(兆)|(億)|(万)", lambda x: "*10**12+" if x.group(1) else "*10**8" if x.group(2) else "*10**4", sales_figure)
        return eval(hennkan)



def convert_eps(eps_figure: str) -> int:
    number_str = eps_figure.split('円')[0]
    hennkan = number_str + '*100'
    return eval(hennkan)


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
    

def convert_stock(stock_price: str) -> str:
    if '.' in stock_price:
        number_str = stock_price.split('円')[0]
        integer_part, decimal_part = number_str.split('.')
        integer_part = integer_part.zfill(2)
        decimal_part = decimal_part.zfill(2)
        return f"{integer_part}.{decimal_part}"
    elif '*' in stock_price:
        kn = stock_price.split('*')[1]
        number_str1 = kn .split('円')[0]
        integer_part1 = number_str1.zfill(2)
        return f"{integer_part1}.00"
    else:
        number_str = stock_price.split('円')[0]
        integer_part = number_str.zfill(2)
        return f"{integer_part}.00"



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

def process_cashes(cashes):
    cash_list = [cash.text for cash in cashes]
    eval_cash_list = []
    for cash in cash_list:
        # 兆しかない時
        if '兆' in cash and '億' not in cash and '万' not in cash:
            hennkan = cash.replace('兆', '*10**12')
            eval_cash_list.append(eval(hennkan))
        # 億しかない時
        elif '億' in cash and '兆' not in cash and '万' not in cash:
            hennkan = cash.replace('億', '*10**8')
            eval_cash_list.append(eval(hennkan))
        # 万しかない時
        elif '万' in cash and '兆' not in cash and '万' not in cash:
            hennkan = cash.replace('万', '*10**4')
            eval_cash_list.append(eval(hennkan))
        # 兆と億の時
        elif '兆' in cash and '億' in cash:
            hennkan = cash.replace('兆', '*10**12+').replace('億','*10**8')
            eval_cash_list.append(eval(hennkan))
        # 億と万の時
        elif '億' in cash and '万' in cash:
            hennkan = cash.replace('億', '*10**8+').replace('万','*10**4')
            eval_cash_list.append(eval(hennkan))
        else:
            hennkan = re.sub(r"(兆)|(億)|(万)", lambda x: "*10**12+" if x.group(1) else "*10**8" if x.group(2) else "*10**4", sale)
            eval_cash_list.append(eval(hennkan))
    return eval_cash_list


import re

def process_cfflows(cfflows):
    cf_flow_list = [cfflow.text for cfflow in cfflows]
    eval_cf_flow_list = []
    for flow in cf_flow_list:
        # 兆しかない時
        if '兆' in flow and '億' not in flow and '万' not in flow:
            hennkan = flow.replace('兆', '*10**12')
            eval_cf_flow_list.append(eval(hennkan))
        # 億しかない時
        elif '億' in flow and '兆' not in flow and '万' not in flow:
            hennkan = flow.replace('億', '*10**8')
            eval_cf_flow_list.append(eval(hennkan))
        # 万しかない時
        elif '万' in flow and '兆' not in flow and '万' not in flow:
            hennkan = flow.replace('万', '*10**4')
            eval_cf_flow_list.append(eval(hennkan))
        # 兆と億の時
        elif '兆' in flow and '億' in flow:
            hennkan = flow.replace('兆', '*10**12+').replace('億','*10**8')
            eval_cf_flow_list.append(eval(hennkan))
        # 億と万の時
        elif '億' in flow and '万' in flow:
            hennkan = flow.replace('億', '*10**8+').replace('万','*10**4')
            eval_cf_flow_list.append(eval(hennkan))
        else:
            hennkan = re.sub(r"(兆)|(億)|(万)", lambda x: "*10**12+" if x.group(1) else "*10**8" if x.group(2) else "*10**4", sale)
            eval_cf_flow_list.append(eval(hennkan))
    return eval_cf_flow_list


def convert_japanese_financial_string(string):
    hennkan = string.replace('兆', '*10**12').replace('億', '*10**8').replace('万', '*10**4')
    return eval(hennkan)



def convert_flow_figure(flow_figure: str) -> int:
        #兆しかない時
        if '兆' in flow_figure and '億' not in flow_figure and '万' not in flow_figure:
            hennkan = flow_figure.replace('兆', '*10**12')
            return eval(hennkan)         
        #億しかない時
        elif '億' in flow_figure and '兆' not in flow_figure and '万' not in flow_figure:
            hennkan = flow_figure.replace('億', '*10**8')
            return eval(hennkan)             
        #万しかない時
        elif '万' in flow_figure and '兆' not in flow_figure and '万' not in flow_figure:
            hennkan = flow_figure.replace('万', '*10**4')
            return eval(hennkan)
        #兆と億の時
        elif'兆'in flow_figure and '億' in flow_figure:
            hennkan = flow_figure.replace('兆', '*10**12+').replace('億','*10**8')
            return eval(hennkan)
        #億と万の時
        elif'億'in flow_figure and '万' in flow_figure:
            hennkan = flow_figure.replace('億', '*10**8+').replace('万','*10**4')
            return eval(hennkan)
        else:
            hennkan = re.sub(r"(兆)|(億)|(万)", lambda x: "*10**12+" if x.group(1) else "*10**8" if x.group(2) else "*10**4", flow_figure)
            return eval(hennkan)


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
def check_uriagedaka(eval_sale_list):
    result = all(int(eval_sale_list[i]) < int(eval_sale_list[i+1]) for i in range(len(eval_sale_list)-1))
    uriagedaka_stock = []
    if result:
        uriagedaka_stock.append('OK')
    else:
        for i in range(len(eval_sale_list)-1):
            if int(eval_sale_list[i]) >= int(eval_sale_list[i+1]):
                uriagedaka_stock.append(f'NOT (at index {i+1})')
    return uriagedaka_stock


def check_eps(zeps_list):
    result = all(int(zeps_list[i]) < int(zeps_list[i+1]) for i in range(len(zeps_list)-1))
    eps_stock = []
    if result:
        eps_stock.append('OK')
    else:
        for i in range(len(zeps_list)-1):
            if int(zeps_list[i]) >= int(zeps_list[i+1]):
                eps_stock.append(f'NOT (at index {i+1})')
    return eps_stock

def check_eiri(zop_list):
    zop_list = [float(x) for x in zop_list]
    resault = all(10 <= float(zop_list[i]) for i in range(len(zop_list)))
    eiri_stock = []
    if resault:
        eiri_stock.append('OK')
    else:
        for i in range(len(zop_list)):
            if 10 >= float(zop_list[i]):
                eiri_stock.append(f'NOT (at index {i})')
    return eiri_stock

def check_zikosihon(zoption_list):
    oolist = [float(x) for x in zoption_list]
    result = all(40 <= float(oolist[i]) for i in range(len(oolist)))
    zikosihon_stock = []
    if result:
        zikosihon_stock.append('OK')
    else:
        for i in range(len(oolist)):
            if 40 >= float(oolist[i]):
                zikosihon_stock.append(f'NOT (at index {i})')
    return zikosihon_stock


def check_genkin(eval_cash_list):
    result = all(int(eval_cash_list[i]) < int(eval_cash_list[i+1]) for i in range(len(eval_cash_list)-1))
    genkin_stock = []
    if result:
        genkin_stock.append('OK')
    else:
        for i in range(len(eval_cash_list)-1):
            if int(eval_cash_list[i]) >= int(eval_cash_list[i+1]):
                genkin_stock.append(f'NOT (at index {i+1})')
    return genkin_stock




def get_closing_url(code):
    url = f'https://irbank.net/{code}/ir'
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text,'html.parser')
    element = soup.select_one('div.csb.cc2 > ul:nth-of-type(2) > li:first-of-type')
    taget = element.find('a')
    link = taget.get('href')
    return link


# In[363]:





# In[429]:


@tictoc
@cache
def get_closing_url(code):
    url = f'https://irbank.net/{code}/ir'
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text,'html.parser')
    element = soup.select_one('div.csb.cc2 > ul:nth-of-type(2) > li:first-of-type')
    taget = element.find('a')
    link = taget.get('href')
    return link


# In[ ]:





# In[ ]:


from bs4 import BeautifulSoup
import requests 
import re
from time import sleep
import pandas as pd

url='https://irbank.net/E02288/results'
sleep(2)
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
title=soup.find('h1').text
ds = soup.find_all('h2')

text=[]
for element in ds:
    for a in element.find_all('a'):
        a.decompose()
    text.append(element)
   #-------------------------------------------------------------------------ひとまず終了------------------------------------------------------------------------#    


   #-------------------------------------------------------------------------ひとまず終了------------------------------------------------------------------------#
target_h2 = []#正規は８項目
for t in text:
    if "売上高" in t or"EPS" in t or "営業利益率" in t or "自己資本比率" in t or "現金等" in t or "営業活動によるCF" in t or "一株配当" in t or "配当性向" in t:
        target_h2.append(t)
    
test__lists=[]
if len(target_h2)==8:
    for i in target_h2:
        bro=i.find_next_sibling()
        ss = bro.find_all('span', class_='text')
        test__lists.append(ss)
else:
    test__lists.append( len(target_h2))


# In[ ]:


test__lists


# In[ ]:


target_h2 = []
for t in text:
    if ("売上高" in t) and ("EPS") in t and ("営業利益率") in t and ("自己資本比率") in t and ("現金等") in t and ("営業活動によるCF") in t and ("一株配当") in t and ("配当性向") in t:
        target_h2.append(t)
    else:
        target_h2.append('none')
        
        
# ore=['売上高','EPS','営業利益率','自己資本比率','現金等','営業活動によるCF','一株配当','配当性向']

test__lists=[]
if len(target_h2)==8:
    for i in target_h2:
        bro=i.find_next_sibling()
        ss = bro.find_all('span', class_='text')
        test__lists.append(ss)
else:
    test__lists.append(len(target_h2))


# In[155]:


import requests
from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache

session = requests.Session()
# sessionをラップしたcached_sessionを作る。
# キャッシュはファイルとして .webcache ディレクトリ内に保存する。
cached_session = CacheControl(session, cache=FileCache('.webcache'))

response = cached_session.get('https://irbank.net/E31167/results') 

# response.from_cache属性でキャッシュから取得されたレスポンスかどうかを取得できる。
print(f'from_cache: {response.from_cache}') 
print(f'status_code: {response.status_code}')


# In[132]:





# In[180]:


from logging import getLogger,StreamHandler,DEBUG,ERROR

logger=getLogger(__name__)
handler=StreamHandler()
handler.setLevel(ERROR)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.debug('これはデバッグログ')


# In[195]:


securities_codes = get_securities_codes(27,28)
for x in securities_codes:
    with open('irbank/csv/securities_codes.pickle','wb') as f:
        pickle.dump(x,f)
    with open('irbank/csv/securities_codes.pickle','rb') as f:
        x=pickle.load(f)
print(x)


# In[418]:





# In[420]:


print(len(existing_data))


# In[421]:


for key in existing_data:
    print(key, existing_data[key])


# In[424]:



import itertools

flattened_codes = list(itertools.chain(*existing_data.values()))
print(len(flattened_codes))


# In[422]:


# num_keys = len(existing_data)
# print(num_keys)
del existing_data[39]


# In[ ]:





# In[205]:


import time

# 関数の実行時間を測るデコレータ
def tictoc(func):
    def _wrapper(*args, **keywargs):
        start_time = time.time()
        result = func(*args, **keywargs)
        print('time: {:.9f} [sec]'.format(time.time() - start_time))
        return result
    return _wrapper


# In[206]:


from functools import cache

@tictoc
@cache  # デコレータを付与
def func(num):
    # なんらかの重い処理
    for _ in range(1000000):
        num += 1
    return num

# 1度目の呼び出し
func(1)

# 2度目の呼び出し
func(1)


# In[207]:


func(1)


# In[404]:





# In[214]:


securities_codes = get_securities_codes(27,28)


# In[444]:


dic


# In[442]:





# In[439]:


ex_data


# In[395]:


closing_url = list(closing_dict.values())
#ここまでclosing_dict


# In[440]:


del ex_data[0]


# In[ ]:


#gptへの質問2023/01/10

result = {}
for page in range(35, 38):
    securities_codes = get_securities_codes(page, page)
    result[page] = securities_codes
    if os.path.exists('irbank/csv/securities_codes.pickle'):
     # ファイルから既存のデータを読み込む
        with open('irbank/csv/securities_codes.pickle', 'rb') as f:
            existing_data = pickle.load(f)
        # 既存のデータを更新する
        existing_data.update(result)
        # ファイルに追加されたデータを保存する
        with open('irbank/csv/securities_codes.pickle', 'wb') as f:
            pickle.dump(existing_data, f)
    else:
        with open('irbank/csv/securities_codes.pickle', 'wb') as f:
            pickle.dump(result, f)

for key in existing_data:
    print(key, existing_data[key])
flattened_codes = list(itertools.chain(*existing_data.values()))こららの中に無駄な作業はありますか？

