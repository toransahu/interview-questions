'''
Created on 30-Nov-2016

@author: toran
'''
from multiprocessing import Process
import os
import Queue

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    q=Queue.Queue()
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()