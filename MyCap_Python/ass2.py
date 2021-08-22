# -*- coding: utf-8 -*-
"""
@author: Acno-Aamir
"""
import string
import random
def q1():
    print("-----------------------------------------------------------")
    print("Q1 While and For loop - implement break and continue statement")
    
    # WHILE LOOP
    n = random.randint(0,10)
    x=int(input("There is a random number x which lies between 0 and 10. Guess which number it is "))
    while(x!=n):
        x=int(input("Sorry thats not the correct answer, so choose another number "))
        
    #FOR LOOP
    n = random.randint(0,10)
    print("\n\nNow the computer plays")
    for i in range(10):
        print("Trying for ",i)
        if i==n:
            print("The random number was ",i)
            break
    
    #Break and continue
    print("\n\nCount from 0-20 and if a number is divisible by 18 break, if its divisible by 4 do not print ")
    
    for i in range(20):
        if i==18:
            break
        elif i%4==0:
            print("\t",end="")
            continue
        else:
            print(i,end="\t")
def q2():
    print("-----------------------------------------------------------")
    print("Q2 For loop - create the following star triangle pattern using For Loop only")
    n=int(input("Enter the number of rows for the patern "))
    k=n-1
    for i in range(n):
        for j in range(k):
            print("",end=" ")
        k-=1
        for j in range(i+1):
            print("*",end=" ")
        print("")

def q3():
    print("-----------------------------------------------------------")
    print("Q3. W3schools - Dictionary methods ")
    #str=input("Enter a string ")
    upper={}
    lower={}
    char={}
    for i in range(65,91):
        z=chr(i)
        upper[z]=i
        char[z]=i
    for i in range(97,123):
        z=chr(i)
        lower[z]=i
        char[z]=i
    print("Dictionary containing Upper char called upper ",upper)
    print("\nDictionary containing Lower char called lower ",lower)
    print(char)
    # 1 copy
    upper1=upper.copy()
    print("\n\nUpper1 coppies upper ",upper1)
    # 2 clear
    upper1.clear()
    print("\n\nupper1 gets cleared ",upper1)
    # 3 get
    s=list(input("Using get\nEnter a string "))
    print(s)
    for z in s:
        print(z," : ",char.get(z))
    # 4 items
    print("\n\nItems of lowers are ",lower.items())
    # 5 keys
    print("\n\nKeys of lowers are ",lower.keys())
    # 6 Values
    print("\n\nValues of lowers are ",lower.values())
    # 7 pop
    s=list(input("\n\nUsing pop\nEnter a upper case char "))
    upper.pop(s[0])
    print("\n\nAfter popping ",s[0]," we get ",upper)
    # 8 popitem
    upper.popitem()
    print("\n\nAfter using popitem we get ",upper)
    # 9 update
    print("\n\nReducing the values of all items in lower by 1 using update")
    for i in lower:
        lower.update({i:(lower[i]-1)})
    print(lower)
    # 10 Fromkey
    key=[]
    for i in range(10):
        x=random.choice(string.ascii_letters)
        key.append(x)
    c=dict.fromkeys(key)
    print("\n\nUsing fromkey ",c)
    # 11 setdefault 
    x = c.setdefault("@", "NOPE")
    print("\n\nUsing setdefault ",c)
    print(x)

ch=0
while(ch!=4):
    ch=int(input("Welcome to Assignment 2\nPress 1 for Q1\nPress 2 for Q2\nPress 3 for Q3\nPress 4 to exit "))
    if ch==1:
        q1()
    elif ch==2:
        q2()
    elif ch==3:
        q3()
    elif ch==4:
        break
    else:
        print("Invalid option")
        