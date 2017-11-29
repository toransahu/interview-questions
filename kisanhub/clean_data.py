# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:31:43 2017

@author: toran.sahu
"""

from os.path import join, isfile


def get_data(data_loc):
    """Get downloaded data."""
    from os import listdir

    files = [f for f in listdir(data_loc) if isfile(join(data_loc, f))]
    return files


def clean_data():
    """Clean downloaded data."""
    import platform

    if platform.system == 'Windows':
        data_loc = '.\data'
    else:
        data_loc = './data'

    files = get_data(data_loc)

    for file in files:
        file_loc = join(data_loc, file)
        # read file
        with open(file_loc, 'r') as f:
            lines = f.readlines()

        # remove first 7 lines
        # write lines to the file
        with open(file_loc, 'w') as f:
            lines = lines[7:]
            f.writelines(lines)


clean_data()
