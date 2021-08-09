# -*- coding: utf-8 -*-
"""
@author: Acno-Aamir
"""

x=list(map(int,input("Enter the list of values seperated by , (Pls do not add []) ").split(",")))
# print(x)
pos=[]
neg=[]
for i in x:
    if(i>=0):
      pos.append(i)
    else:
      neg.append(i)
print("\n\nThe positive values in the inputs are ",pos)
print("\nThe negative values in the inputs are ",neg)