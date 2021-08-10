# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:54:41 2021

@author: aamir
"""
def most_frequent(word):
    freq={}
    arr=[]
    for i in word:
        if i in arr:
            freq[i]+=1
        else:
            arr.append(i)
            freq[i]=1
    #print(freq)
    m=0
    for i in freq:
        if(freq[i]>m):
            m=freq[i]
    print("")
    for j in range(m):
        for i in freq:
            if(freq[i]==(m-j)):
                print(i," = ",freq[i])
    
word=input("Enter the word/string to give frequencies of : ")
w=list(word)
#print(w)
most_frequent(w)

    