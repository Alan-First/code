#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Harry
import numpy as np

def sigmond(data):


def LogisticRegression(newdata,data,label,lr):#data每行代表不同的数据，列为数据维度;label每行均为标签
    dimension = np.size(data,1)
    num = np.size(data,0)
    w = np.zeros((dimension,1))#列向量
    b = 0
    flag = True#是否需要迭代
    while flag: 
        flag = False#一旦全部都满足条件则跳出循环
        for i in range(num):
            if label[i]*(np.dot(data[i],w)+b)<=0:
                w = w.T+lr*label[i]*data[i]#注意相加之前要转置，不然会合并
                w = w.T
                b = b+lr*label[i]
                flag = True
    
    if any(newdata):
        newlabel = 1 if np.dot(newdata,w)+b>0 else -1
        return newlabel
    else:
        return w,b
        
    
           

if __name__ == "__main__":
    data = np.array([[3,3],[4,3],[1,1]])
    label = np.array([1,1,-1])
    newdata = np.array([])
    w,b = LogisticRegression(newdata,data,label,lr=1)
    print("w=")
    print(w)
    print("b="+str(b))
    



