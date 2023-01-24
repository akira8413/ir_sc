#!/usr/bin/env python
# coding: utf-8

# In[3]:


# %run -i 'modules/get_securities_codes.py'
def get_flattened_codes(start_page, end_page, file_path):
    result = {}
    for page in range(start_page, end_page + 1):
        securities_codes = get_securities_codes(page, page)
        result[page] = securities_codes
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                existing_data = pickle.load(f)
            existing_data.update(result)
            with open(file_path, 'wb') as f:
                pickle.dump(existing_data, f)
        else:
            with open(file_path, 'wb') as f:
                pickle.dump(result, f)

    with open(file_path, 'rb') as f:
                existing_data = pickle.load(f)
    flattened_codes = list(itertools.chain(*existing_data.values()))
    return flattened_codes






