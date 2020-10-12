#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Harry
import numpy as np
import math

def sigmond(data):
    return 1/(1+math.exp(-data))


def LogisticRegression(newdata,data,label,lr,max_iter=100):#data每行代表不同的数据，列为数据维度;label每行均为标签
    times = 0
    dimension = np.size(data,1)
    num = np.size(data,0)
    #w = np.zeros((dimension,1))#列向量
    #b = 0
    flag = True#是否需要迭代
    data = np.column_stack((data,np.ones((num,1))))
    w = np.zeros((dimension+1,1))#列向量
    while times < max_iter: 
        #flag = False#一旦全部都满足条件则跳出循环
        for i in range(num):
        #if label[i]*(np.dot(data[i],w)+b)<=0:
            result = sigmond(np.dot(data[i],w))#列向量
            w = w.T+lr*data[i]*result#注意相加之前要转置，不然会合并
            w = w.T
        times+=1
    
    if any(newdata):
        
        newdata = np.append(newdata,1)
        print(newdata)
        newlabel = 1 if sigmond(np.dot(newdata,w))>0.5 else 0
        return newlabel
    else:
        return w
        
    
           

if __name__ == "__main__":
    data = np.array([[3,3],[4,3],[1,1]])
    label = np.array([1,1,-1])
    newdata = np.array([3,3])
    w = LogisticRegression(newdata,data,label,lr=1)
    print("w=")
    print(w)
    
