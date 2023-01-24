#!/usr/bin/env python
# coding: utf-8

def extract_data(target_h2_stringso, all_title):
    test_lists = []
    titles = []
    false = []
    try:
        for uu, title1 in zip(target_h2_stringso, all_title):
            if len(uu) == 8:
                test_lists.append([i.find_next_sibling().find_all('span', class_='text') for i in uu])
                titles.append(title1)
            else:
                false.append({"企業名":title1,"評価":uu})
    except ValueError:
        print("The number of elements in target_h2_stringso and all_title are not equal.")
        return [], [], []
    return test_lists, titles, false
