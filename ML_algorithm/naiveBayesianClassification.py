#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
def Bayes(newdata,data,label,bayes):#data每行是一个数据，每列是一个维度；newdata是个向量
    result = {}#字典。键是结果，值是对应的可能性
    dimension = np.size(data,1)#数据总维度
    label_num,label_pro = labelProbb(label,bayes)#字典，label_num键为label值，值为对应数目；label_pro键为label值，值为概率
    even_probb = {}#字典，键为(维度，值，label值)，值为对应条件概率
    data_value_num = {}#字典，键是数据的维度数，值是取值范围总数
    lpls = 1 if bayes else 0#是否使用拉普拉斯平滑，是则为贝叶斯估计，否则为最大似然估计
    
    '''统计条件概率所需的总数目'''
    for i in range(np.size(data,0)):
        for j in range(dimension):
            even_probb[(j,data[i][j],label[i])]=0
    for i in range(np.size(data,0)):
        for j in range(dimension):
            even_probb[(j,data[i][j],label[i])]+=1
    
    '''统计贝叶斯估计所需：各维度可能取值的总数'''      
    for i in range(dimension):
        dataset = set(data[:,i])
        data_value_num[i] = len(dataset)
    
    '''统计条件概率'''
    for i in label_pro.keys():
        for j in range(dimension):
            for k in set(data[:,j]):
                even_probb[(j,k,i)] = (even_probb[(j,k,i)]+lpls)/(label_num[i]+data_value_num[j]*lpls)
                print(str((j,k,i))+"条件概率为"+str(even_probb[(j,k,i)]))
    
    '''计算新数据从属各个分类的可能性'''
    for i in label_pro.keys():
        result[i] = label_pro[i]
        for j in range(dimension):
            result[i] = result[i]*even_probb[(j,newdata[j],i)]
    
    for i in label_pro.keys():
        print("i="+str(i)+"可能性:"+str(result[i]))
    
    return max(result,key=result.get)
    
def labelProbb(label,bayes):
    lpls = 1 if bayes else 0
    label_num = {}
    label_rate = {}
    for i in label:
        label_num[i] = 0
    for i in label:
        label_num[i] += 1
    for i in label_num.keys():
        label_rate[i] = (label_num[i]+lpls)/(len(label)+lpls*len(set(label)))
        print(str(i)+"有"+str(label_rate[i])+"个")
        
    
    return label_num,label_rate    
    
if __name__ == "__main__":
    li = [["1","s"],["1","m"],["1","m"],["1","s"],["1","s"],["2","s"],["2","m"],["2","m"],["2","l"],["2","l"],
    ["3","l"],["3","m"],["3","m"],["3","l"],["3","l"]]
    x = np.array(li)
    
    y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    data = ["2","s"]
    sort = Bayes(newdata=data,data=x,label=y,bayes=False)
    print(sort)
        
