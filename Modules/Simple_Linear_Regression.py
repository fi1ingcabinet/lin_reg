'''
Created on 17 Sep 2018
Simple Linear Regression Function, input a csv, specify which 2 numeric parameters and go
@author: root
'''
import csv
from matplotlib import pyplot as plt
from sklearn import linear_model as lm
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
import numpy as np

def enter_file_path():
    path=input("enter a file path: ")
    return path

def read_column_csv(path,i):
    numbers=[]
    with open(path) as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
                numbers.append(float((row[i])))
    return numbers

def pick_columns_as_list():
    path=enter_file_path()
    x=int(input("Please specify which is the x variable: "))
    y=int(input("Please specify which is the y variable: "))
    
    numbers1=[]
    numbers1=read_column_csv(path,x)
    numbers2=[]
    numbers2=read_column_csv(path,y)
    
    return numbers1, numbers2

def plot(x, y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    #print(numbers2)

    plt.xticks(np.arange(0,len(x),step=len(x)/10+1)) 
    plt.yticks(np.arange(0,len(y),step=len(y)/10+1))    
    plt.scatter(numbers1[0:],numbers2[0:])
    plt.show()

def lin_reg_line(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    regr=lm.LinearRegression()
    regr.fit(numbers1,numbers2)
    print(regr.coef_, regr.intercept_)

    plt.plot(numbers1,regr.coef_[0][0]*numbers1+regr.intercept_[0],color='C1')

def manual_lin_reg_line(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    x_tot=0
    y_tot=0
    for i in range(1,len(numbers1)+1):
        x_tot=x_tot+numbers1[i-1:i]
    for i in range(1,len(numbers2)+1):
        y_tot=y_tot+numbers2[i-1:i]
    x_bar=x_tot/len(numbers1)
    y_bar=y_tot/len(numbers2)
    a_1=0
    a_2=0
    for i in range(1,len(numbers1)+1):
        a_1=a_1+(numbers1[i-1:i]*numbers2[i-1:i]-numbers1[i-1:i]*y_bar)
        a_2=a_2+(numbers1[i-1:i]**2-numbers1[i-1:i]*x_bar)
        #print(a_1,a_2)
        #print(numbers1[i-1:i],numbers2[i-1:i])
    a=a_1/a_2
    b=y_bar-a*x_bar
    
    print(a,b)

def np_variance(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    variance=np.var(numbers2[0:])
    #print(variance)
    return variance

def manual_variance(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    sum_x=0
    for i in range(1,len(numbers2)+1):
        sum_x=sum_x+numbers2[i-1:i]
    mu=sum_x/len(numbers2)
    
    sum_x_minus_mu=0
    for i in range(1,len(numbers2)+1):
        sum_x_minus_mu=sum_x_minus_mu+(numbers2[i-1:i]-mu)**2
    
    var=sum_x_minus_mu/len(numbers2)    
    #print(var)
    return var
    
def sklearn_r_squared(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    regr=lm.LinearRegression()
    regr.fit(numbers1,numbers2)
    
    y_pred=[]
    for i in range(1,len(numbers2)+1):
        y_pred.append(regr.coef_*numbers2[i-1:i]+regr.intercept_)
    y_pred=np.asanyarray(y_pred)
    y_pred=y_pred.reshape(-1, 1)
    r_sq=r2_score(numbers2[0:],y_pred)
    print(r_sq)

def manual_r_squared(x,y):
    numbers1=np.asanyarray(x)
    numbers1=numbers1.reshape(-1, 1)
    #print(numbers1)
    numbers2=np.asanyarray(y)
    numbers2=numbers2.reshape(-1, 1)
    
    regr=lm.LinearRegression()
    regr.fit(numbers1,numbers2)
    y_pred=[]
    for i in range(1,len(numbers2)+1):
        y_pred.append(regr.coef_*numbers2[i-1:i]+regr.intercept_)
    
    y_diff=[]
    for i in range(1,len(numbers2)+1):
        y_diff.append((numbers2[i-1:i]-y_pred[i-1]))
    
    #print(manual_variance(x,y),manual_variance(x, y_diff))
    
    manual_r_2=(np_variance(x,y)-np_variance(x, y_diff))/np_variance(x,y)
    manual_r=manual_r_2**2
    man_3=np_variance(x,y_pred)/np_variance(x, y)
    man_4=np.var(y_pred)/np.var(y)
    man5=regr.coef_**2*np.var(x)/np.var(y)
    print(manual_r_2,manual_r,man_3,man_4,man5)
    
    
if __name__=='__main__':
    x,y=pick_columns_as_list()
    #plot()
    #lin_reg_line()
    #manual_lin_reg_line()
    #np_variance()
    #manual_variance()
    sklearn_r_squared(x,y)
    manual_r_squared(x,y)
    