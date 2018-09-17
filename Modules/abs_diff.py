'''
Created on 16 Sep 2018

@author: root
'''

import csv
from matplotlib import pyplot as plt
from sklearn import linear_model as lm
import numpy as np

def read_column_csv(path,i):
    numbers=[]
    with open(path) as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
                numbers.append(float((row[i])))
    return numbers




if __name__=='__main__':
    numbers1=np.asanyarray(read_column_csv("/home/marion/Desktop/Random/FuelConsumption.csv",4))
    numbers1=numbers1.reshape(-1, 1)
    print(numbers1)
    numbers2=np.asanyarray(read_column_csv("/home/marion/Desktop/Random/FuelConsumption.csv",12))
    numbers2=numbers2.reshape(-1, 1)
    print(numbers2)
    
    #plt.scatter(numbers1[1:],numbers2[1:])
    #plt.show()
    x_tot=0
    y_tot=0
    #manual calculate regression parameters
    for i in range(1,len(numbers1)+1):
        x_tot=x_tot+numbers1[i-1:i]
    for i in range(1,len(numbers2)+1):
        y_tot=y_tot+numbers2[i-1:i]
    x_bar=x_tot/len(numbers1)
    y_bar=y_tot/len(numbers2)
    a_1=0
    a_2=0
    '''for i in range(1,len(numbers1)+1):
        a_1=a_1+(numbers1[i-1:i]*numbers2[i-1:i]-numbers1[i-1:i]*y_bar)
        a_2=a_2+(numbers1[i-1:i]**2-numbers1[i-1:i]*x_bar)
        print(a_1,a_2)
        #print(numbers1[i-1:i],numbers2[i-1:i])
    a=a_1/a_2
    b=y_bar-a*x_bar
    
    print(x_bar,y_bar,a_1,a_2,a,b)
    
    regr=lm.LinearRegression()
    regr.fit(numbers1,numbers2)
    print(regr.coef_, regr.intercept_)

    #plt.plot(numbers1,regr.coef_[0][0]*numbers1+regr.intercept_[0])
    #plt.show()
    
    numbers3=[]
    numbers4=[]
    for i in range(0,len(numbers1)):
        numbers3.append(regr.coef_[0][0]*numbers1[i]+regr.intercept_[0])
        numbers4.append(numbers3[i]-numbers2[i])
    print(numbers4)
    numbers4=np.asanyarray(numbers4)
    numbers4.reshape(-1, 1)
    
    #plt.scatter(numbers1,numbers4)
    plt.hist(numbers4)
    plt.show()
    '''
    a=[]
    b=[]
    q=0.1
    lim=20
    diff=401
    for i in range(diff):
        a.append(-10+(i*1/lim))
    b=a
    print(a,b)
    
    sum=0
    
    '''for i in a:
        for j in b:
            for k in range(0,len(numbers1)):
                sum=sum+(numbers2[k-1:k]-(i*numbers1[k-1:k]+b))
    print(sum)
    '''
    for k in range(30,40):
        for j in range(120,130):
            for i in range(1,len(numbers1)+1):
                #print(numbers1[i-1:i],numbers2[i-1:i],sum)
                sum=sum+(numbers2[i-1:i]-j*numbers1[i-1:i]-k)
                #print(sum,i,j,k)
            print(sum,i,j,k)
        sum=0
    print(sum)
    #print(sum)
    #plot(numbers1,)
    