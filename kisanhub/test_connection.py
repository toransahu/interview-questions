# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:31:32 2017

@author: toran.sahu
"""

import urllib.request
import os
#import urllib.request

url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/ranked/UK.txt"

proxies = {
    "http": "http://toran.sahu:L440Qthink@10.74.91.103:80",
    "https": "http://toran.sahu:L440Qthink@10.74.91.103:80",
}

#os.environ['NO_PROXY'] = "http://toran.sahu:L440Qthink@10.74.91.103:80"
r = urllib.request.proxy_bypass("http://toran.sahu:L440Qthink@10.74.91.103:80")
urlretrieve(url, filename = "Tmax_UK.txt")

print(r.url)
