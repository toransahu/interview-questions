# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:49:20 2017

@author: toran.sahu
"""


def download_file(url, proxies):
    """Download a file from url as raw"""
    import requests

    res = requests.get(url, stream=True, proxies=proxies)
    return res


def save_file(loc, filename, response):
    """Save a raw file into disk"""
    import os
    import codecs
    file_loc = os.path.join(loc, filename)
    with codecs.open(file_loc, 'w', response.encoding) as f:
        f.write(response.text)


def download_data(regions, attributes):
    """Download all data"""

    import platform

    url_prefix = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets"

    ## check in which pc i'm working
    if platform.system() == 'Windows':
        # loc = "D:\Toran\WorkSpace\practice\interview\kisanhub\data"
        loc = ".\data"
        proxies = {
            "http": "http://toran.sahu:L440Qthink@10.74.91.103:80",
            "https": "http://toran.sahu:L440Qthink@10.74.91.103:80",
        }
    else:
        # loc = "/mnt/ExternalHDD/E/workSpace/practice/interview/kisanhub/data"
        loc = "./data"
        proxies = {
            "http": None,
            "https": None,
        }

    ## download and save all the files
    for region in regions:
        for attribute in attributes:
            url = url_prefix + '/' + attribute + '/' + 'ranked' + '/' + region + '.txt'
            filename = attribute + '_' + region + '.txt'
            # download file
            response = download_file(url, proxies)
            # save file @ ./data/
            save_file(loc, filename, response)


regions = ['UK', 'England', 'Wales', 'Scotland']
attributes = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']
if __name__ == '__main__':
    download_data(regions, attributes)
