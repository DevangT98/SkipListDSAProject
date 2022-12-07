from SkipList import SkipList
import time
import numpy as np
import random

keys = np.arange(0, 200000, 2)
values = np.arange(0, 200000, 2)

dict = SkipList()

start1 = time.time()
for i in range(0, 10000):
    dict.insertElement(keys[i], values[i])

end1 = time.time()

start2 = time.time()
for i in range(10000, 30000):
    dict.insertElement(keys[i], values[i])

end2 = time.time()

print(end1-start1)
print(end2-start2)
