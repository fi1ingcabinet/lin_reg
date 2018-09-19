'''
Created on 17 Sep 2018
This is a list of all the functions
/home/marion/Desktop/Random/Test_data1.csv
@author: root
'''

import Simple_Linear_Regression

def choice():
    print("1. Linear Regression")

def Linear_Regression():
    print("1. Plot")
    print("2. line values")


if __name__=='__main__':
    while True:
        choice()
        a=input()
        if a=='1':
            Linear_Regression()
            b=input()
            if b=='1':
                Simple_Linear_Regression.plot()
            if b=='2':
                Simple_Linear_Regression.lin_reg_line()
