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


def clean_data(data_loc):
    """Clean downloaded data."""

    files = get_data(data_loc)

    for filename in files:
        file = join(data_loc, filename)
        # read file
        with open(file, 'r') as f:
            lines = f.readlines()

        # remove first 7 lines
        # write lines to the file
        with open(file, 'w') as f:
            lines = lines[7:]
            f.writelines(lines)

