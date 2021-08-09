# -*- coding: utf-8 -*-
"""
@author: Acno-Aamir
"""
n=int(input("Enter the number of terms for Fibonacci series "))
f0=0;f1=1;
if(n>=2):
    print(f0,end=" ")
    print(f1,end=" ")
elif(n==1):
    print(f0)
elif(n==0):
    print("\nNULL")
else:
    print("Invalid input")
for i in range(2,n):
    f=f1+f0
    f0=f1
    f1=f
    print(f,end=" ")