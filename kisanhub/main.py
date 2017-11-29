#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:57:13 2017

@author: toran
"""

from download_data import download_data
from clean_data import clean_data
import platform

regions = ['UK', 'England', 'Wales', 'Scotland']
attributes = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']


## check in which pc i'm working
if platform.system() == 'Windows':
    # data_loc = "D:\Toran\WorkSpace\practice\interview\kisanhub\data"
    data_loc = ".\data"
    proxies = {
        "http": "http://toran.sahu:L440Qthink@10.74.91.103:80",
        "https": "http://toran.sahu:L440Qthink@10.74.91.103:80",
    }
else:
    # data_loc = "/mnt/ExternalHDD/E/workSpace/practice/interview/kisanhub/data"
    data_loc = "./data"
    proxies = {
        "http": None,
        "https": None,
    }

if __name__ == '__main__':
    print("Data downloading...")
    download_data(regions, attributes,data_loc,proxies)
    print("Cleaning data..")
    clean_data(data_loc)
    print("Data is ready.")