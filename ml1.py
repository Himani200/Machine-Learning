#!/usr/bin/python3

import  numpy as np

print("Enter the size of the matrix")
a=int(input("enter the no. of rows for array-1: "))
b=int(input("enter the no. of columns for array-1:"))

a1=int(input("enter the no. of rows for array-2: "))
b1=int(input("enter the no. of columns for array-2:"))

x=str(np.random.randint(low=0,high=100,size=(a,b)))  
#random.randint is to generate random integers and low and high are the lower and upper limit for the integers
print(x)
f=open('fml1.txt','a')
f.write(x)
f.write('\n')
f.close()
print("\n")
y=str(np.random.randint(low=0,high=100,size=(a1,b1)))
print(y)         
f=open('fml11.txt','a')
f.write(y)
f.write('\n')
f.close()                                                              
