'''
Created on 30-Nov-2016

@author: toran
'''
from multiprocessing import Process
import os
from posix import getpid, getppid
def f(name):
    print('hello', name,getppid())

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    print(__name__,os.getppid(),getpid())
    p.join()
    p.join()