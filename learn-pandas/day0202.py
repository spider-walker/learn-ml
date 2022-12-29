from array import *
import sys

highest = 0
current = 0
a = array('i', [0,0,0])
with open('./data/input0101.txt') as f:
    lines = f.readlines()

for line in lines:
    if not line.strip().isnumeric():
        if current > a[0]:
            a[2] = a[1]
            a[1] = a[0]
            a[0] = current
            
        elif current > a[1] and current != a[0]:
            a[2] = a[1]
            a[1] = current   
        elif current > a[2] and current != a[1]:
            a[2] = current        
        current = 0
    else:
        current += int(line)


print(a[0]+a[1]+a[2])
