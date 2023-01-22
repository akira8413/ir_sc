#!/usr/bin/env python
# coding: utf-8


import pickle
from functools import cache
from bs4 import BeautifulSoup
import requests 
import re
import time
from time import sleep
import pandas as pd
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

def get_yeild_curve(code):

    url = f'https://irbank.net/{code}/ir'
    r = requests.get(url)
    sleep(random.uniform(3, 8)) 
    soup = BeautifulSoup(r.text,'html.parser')
    element = soup.select('div.csb.cc2 > ul:nth-of-type(2) > li:nth-of-type(7)')
    for ec in element:
        taget = ec.find('a')
        link = taget.get('href')
    return link

