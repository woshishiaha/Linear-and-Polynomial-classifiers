# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:27:00 2019

@author: SKX
"""


'''
import numpy

newData = numpy.loadtxt('linear.txt')
'''
'''
file=open('linear.txt')    
dataMat=[]  
labelMat=[]
c = 0
for line in file.readlines():
    if c < 200:   
        c = c+1
        curLine=line.strip().split(",")    
        floatLine=curLine#这里使用的是map函数直接把数据转化成为float类型    
        if floatLine[-1] == 'g':
            floatLine[-1] = 1
        else:
            floatLine[-1] = -1
        dataMat.append(list(map(float,floatLine[0:35]))) 
    else:
        curLine=line.strip().split(",")    
        floatLine=curLine#这里使用的是map函数直接把数据转化成为float类型    
        if floatLine[-1] == 'g':
            floatLine[-1] = 1
        else:
            floatLine[-1] = 0
        labelMat.append(list(map(float,floatLine[0:35]))) 
    #dataMat.append(floatLine[-1])


    
print('dataMat:',dataMat)
print('labelMat:',labelMat)
print(np.shape(dataMat))
print(np.shape(labelMat))
'''


import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]

w1x1 + w2x2 + w3 = 0

w1x1 = -w2x2-w3
x1 = (-w2x2-w3)/a

