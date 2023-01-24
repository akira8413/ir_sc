#!/usr/bin/env python
# coding: utf-8

# In[1]:




def main_yeild_data(flatyeild_urls, start, end):
    focus_urls=[]
    all_text=[]
    all_title=[]
    for flatyeild_url in flatyeild_urls[start:end]:
        url='https://irbank.net{}'.format(flatyeild_url)
        sleep(random.uniform(3, 8)) 
        focus_urls.append(url)
        r=requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title=soup.find('h1').text
        all_title.append(title)
        suii=soup.find(id='g_3')
        numv=suii.find_all('span', class_='text')
        all_text.append(numv)
    return focus_urls, all_text, all_title

# flatyeild_urls = [#list of urls]
# num_urls = 50
# focus_urls, all_text, all_title = main_yeild_data(flatyeild_urls, start, end)
    
    
# def main_yeild_data(flatyeild_urls, start, end):
#     focus_urls1=[]
#     all_text1=[]
#     all_title1=[]
#     for flatyeild_url in flatyeild_urls[start:end]:
#         url='https://irbank.net{}'.format(flatyeild_url)
#         sleep(random.uniform(3, 8)) 
#         focus_urls1.append(url)
#     for focus_url1 in focus_urls1:
#         r1=requests.get(focus_url1)
#         soup1 = BeautifulSoup(r1.text, 'html.parser')
#         title1=soup1.find('h1').text
#         all_title1.append(title1)
#         suii=soup1.find(id='g_3')
#         numv=suii.find_all('span', class_='text')
#         all_text1.append(numv)
#     return focus_urls1, all_text1, all_title1

