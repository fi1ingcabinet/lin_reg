'''
Created on 8 Sep 2018

@author: root
'''
'''Simple Linear Regression'''
import csv
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random
from sklearn import linear_model as lm
'''First Import the data'''
def read_csv(path):
    numbers=[]
    squared=[]
    with open(path) as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[5]))
            squared.append(float(row[4]))
    return numbers,squared

if __name__=='__main__':
    test=read_csv()
    #plt.scatter(test[0],test[1])
    
    df = pd.read_csv("/home/marion/Desktop/Random/FuelConsumption2.csv")
    df.head()
    #print(df)
    #df.describe()
    #print(df.describe())
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    cdf.head(9)
    #print(cdf.head(9))
    viz=cdf[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    #print(viz)
    #viz.hist()
    #plt.show()
    
    #
    #plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("FUELCONSUMPTION_COMB")
    plt.ylabel("Emission")
    #plt.show()

    #plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    #plt.show()
    
    #plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
    plt.xlabel("CYLINDERS")
    plt.ylabel("Emission")
    #plt.show()
    
    msk = np.random.rand(len(df)) < 0.8
    #print("msk = ", msk)
    train = cdf[msk]
    #print("train = ",train)
    test = cdf[~msk]
    #print(test)
    
    plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS,color='b')
    plt.xlabel("Eng size")
    plt.ylabel("Emissions")
    #plt.show()
    
    regr=lm.LinearRegression()
    train_x=np.asanyarray(train[['ENGINESIZE']])
    train_y=np.asanyarray(train[['CO2EMISSIONS']])
    regr.fit(train_x,train_y)
    print(regr.coef_)
    print(regr.intercept_)
    print(train_x)
    
    plt.plot(train_x,regr.coef_[0][0]*train_x+regr.intercept_[0],'-r')
    plt.show()