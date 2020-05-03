import numpy as np
import random

N = 10

item = random.sample(range(1, 100), N)
index = []

for i in range(N):
    index.append(i)
    i+=1

def union(a, b):
    a_id = item.index(a)
    b_id = item.index(b)
    a_index = index[a_id]
    b_index = index[b_id]
    
    for i in range(len(index)):
        if index[i] == a_index:
            index[i] = b_index
        i+=1
    print(item)
    print(index)
    return index

def connect(a,b):
    a_id = item.index(a)
    b_id = item.index(b)
    a_index = index[a_id]
    b_index = index[b_id]
    return a_index == b_index