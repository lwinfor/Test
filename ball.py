import os


min = 100
index = 0
for i in range(1,100):
    step = i - 1  + (100/i) - 1
    if step < min:
        min = step
        index = i

print(min,index)