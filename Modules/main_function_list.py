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
    print("1. input csv plot")
    print("2. Lin reg line sklearn input csv")
    print("3. Manual lin reg line input csv")
    print("4. numpy variance")
    print("5. manual variance")
    print("6. sklearn r squared")
    print("7. manual r squared")


if __name__=='__main__':
    while True:
        choice()
        a=input()
        if a=='1':
            Linear_Regression()
            b=input()
            if b=='1':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.plot(x,y)
            if b=='2':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.lin_reg_line(x,y)
            if b=='3':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.manual_lin_reg_line(x,y)
            if b=='4':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.np_variance(x,y)
            if b=='5':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.manual_variance(x,y)
            if b=='6':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.sklearn_r_squared(x,y)
            if b=='7':
                x,y=Simple_Linear_Regression.pick_columns_as_list()
                Simple_Linear_Regression.manual_r_squared(x,y)
