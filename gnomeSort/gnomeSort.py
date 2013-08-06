# -*- coding utf-8 -*-
import random

def gnomeSort(arr):
    i=1
    j=0
    while i<=len(arr)-1:
        if arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
        else:
            i+=1
            j+=1
    print(arr)

arr=[random.randint(0,1000) for i in range(random.randint(10,20))]

print(len(arr))
print(arr)
gnomeSort(arr)
input()
