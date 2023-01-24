#!/usr/bin/env python
# coding: utf-8

# In[1]:



def main_data(flatclosing_urls, start, end):
    focus_url = []
    all_title = []
    all_text = []
    for flatclosing_url in flatclosing_urls[start:end]:
        url = 'https://irbank.net{}'.format(flatclosing_url)
        sleep(random.uniform(3, 8)) 
        focus_url.append(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find('h1').text
        all_title.append(title)
        decopo = soup.find_all('a')
        for a in decopo:
            a.decompose()
        tagget = soup.find_all('h2')
        all_text.append(tagget)
    return focus_url, all_title, all_text


# In[ ]:




