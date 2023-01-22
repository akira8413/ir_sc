
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
def tictoc(func):
    def _wrapper(*args, **keywargs):
        start_time = time.time()
        result = func(*args, **keywargs)
        print('time: {:.9f} [sec]'.format(time.time() - start_time))
        return result
    return _wrapper

@tictoc
@cache
def get_closing_url(code):
    url = f'https://irbank.net/{code}/ir'
    r = requests.get(url)
    sleep(random.uniform(3, 8)) 
    soup = BeautifulSoup(r.text,'html.parser')
    element = soup.select_one('div.csb.cc2 > ul:nth-of-type(2) > li:first-of-type')
    taget = element.find('a')
    link = taget.get('href')
    return link
