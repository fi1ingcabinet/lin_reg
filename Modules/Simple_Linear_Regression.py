'''
Created on 17 Sep 2018
Simple Linear Regression Function, input a csv, specify which 2 numeric parameters and go
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

def plot():
    path=input("enter a file path of csv: ")
    n=int(input("specify x column: "))
    m=int(input("specify y column: "))
    numbers1=np.asanyarray(read_column_csv(path,n))
    numbers1=numbers1.reshape(-1, 1)
    print(numbers1)
    numbers2=np.asanyarray(read_column_csv(path,m))
    numbers2=numbers2.reshape(-1, 1)
    print(numbers2)
    
    plt.scatter(numbers1[1:],numbers2[1:])
    plt.show()

def lin_reg_line():
    path=input("enter path")
    numbers1=np.asanyarray(read_column_csv(path,4))
    numbers1=numbers1.reshape(-1, 1)
    numbers2=np.asanyarray(read_column_csv(path,12))
    numbers2=numbers2.reshape(-1, 1)
    
    regr=lm.LinearRegression()
    regr.fit(numbers1,numbers2)
    print(regr.coef_, regr.intercept_)

    plt.plot(numbers1,regr.coef_[0][0]*numbers1+regr.intercept_[0])
    print("poo")

if __name__=='__main__':
    #plot()
    lin_reg_line()
