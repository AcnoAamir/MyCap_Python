# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:28:20 2021

@author: aamir
"""
import random
def list_gen(m):
    l=[]
    for i in range(m):
        n=random.randint(-1000,1000)
        l.append(n)
    return l

list0=list_gen(10)
print("The is list is \nList0 : ",list0)

list0.append(0)
print("The is list after appending 0 \nList0 : ",list0)

list1=list0.copy()
print("List 1 copies list 0 \nList1 : ",list1,"\nList0 : ",list0)

list0.clear()
print("The is list after clearing \nList0 : ",list0)

n=random.randint(0,len(list1)-1)
x=list1[n]
print("Count of ",x," in list 1",list1.count(x))

list0=list_gen(5)
list1.extend(list0)
print("List 1 extends list 0 \nList1 : ",list1,"\nList0 : ",list0)

n=random.randint(0,len(list1)-1)
x=list1[n]
print("Index of ",x," in list 1",list1.index(x))

n=random.randint(0,len(list1)-1)
m=random.randint(-1000, 1000)
list1.insert(n,m)
print("List1 after Inserting",m," in ",n,"th position\nList1",list1)

n=random.randint(0,len(list1)-1)
list1.pop(n)
print("List1 after popping in ",n,"th position\nList1",list1)

n=random.randint(0,len(list1)-1)
x=list1[n]
list1.remove(x)
print("List1 after removing ",x,"th position\nList1",list1)

list1.sort()
print("List1 after sorting\nList1",list1)

list1.reverse()
print("List1 after reversing \nList1",list1)
