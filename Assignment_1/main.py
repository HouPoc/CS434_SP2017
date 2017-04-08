#!/usr/bin/python
'''
Date: 4/7/2017
Author: Wenbo Hou
The Program aims to implement the linear regression with matrix knowledge
'''
from library import *
import numpy as np

def solution():
    #Load data
    train_data = 'housing_train.txt'
    test_data = 'housing_test.txt'
    data = read_data(train_data)
   
    #Assign Data to correct matrix
    data_x = data[0]
    data_y = data[1]
    for row in data_x:
        row.append(1)
    Xmatrix = np.array(data_x)
    Ymatrix = np.transpose(data_y)

    #W = Inverse(X_t*X) * X_t*y
    Xmatrix_Transpose = np.transpose(Xmatrix)
    Product_X_t_X = Xmatrix_Transpose.dot(Xmatrix)
    Product_Inverse = np.linalg.inv(Product_X_t_X)
    Second_Product = Product_Inverse.dot(Xmatrix_Transpose)
    W = Second_Product.dot(Ymatrix)
    
    #Find SSE (y-x*w)^2
    Matrix_Subtraction = Ymatrix - Xmatrix.dot(W) 
    SSE_dummy = (np.transpose(Matrix_Subtraction)).dot(Matrix_Subtraction)
    print (SSE_dummy)

def main ():
    solution()

if __name__ == "__main__":
    main()    
    

    
