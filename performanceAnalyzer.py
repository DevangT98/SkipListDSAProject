from SkipList import SkipList
import time
import numpy as np
import random

# Created an array of 100,000 size from 0 upto 200,000 so that when created
# test cases for ClosesKeyBefore & ClosestKeyAfter it is easier to implement

keys = np.arange(0, 200000, 2)
values = np.arange(0, 200000, 2)


dict = SkipList()

# Analysis for Insertion

# for first 10000 key-value pair

start1 = time.time()
for i in range(0, 10000):
    dict.insertElement(keys[i], values[i])

end1 = time.time()


# Search operation in a 10000-key skiplist

# Successful attempt

k = random.randrange(0, 10000, 2)
val = dict.findElement(k)

# Unsuccessful attempt

uk = random.randrange(1, 10000, 2)
val = dict.findElement(uk)

# Search for ClosestKeyBefore Operation in a 10,000-key SkipList

uk = random.randrange(1, 10000, 2)
val = dict.closestKeyBefore(uk)


# Search for ClosestKeyAfter Operation in 10,000-key SkipList

uk = random.randrange(1, 10000, 2)
val = dict.closestKeyAfter(uk)

# for the second 10000 key-value pair to analyse after 10000 pair insertion

# start2 = time.time()
# for i in range(10000,20000):
#     dict.insertElement(keys[i],values[i])
#
# end2 = time.time()

# Search operation in a 20000-key SkipList
#
# Successful attempt

k = random.randrange(0, 10000, 2)
val = dict.findElement(k)

# Unsuccessful attempt

uk = random.randrange(1, 10000, 2)
val = dict.findElement(uk)


# for the third 10000 key-value pair to analyse after 20000 pair already there
#
# start3 = time.time()
# for i in range(20000,30000):
#     dict.insertElement(keys[i],values[i])
#
# end3 = time.time()
#
# # for next 20000 key-value pair
#
# start4 = time.time()
# for i in range(30000,50000):
#     dict.insertElement(keys[i],values[i])
#
# end4 = time.time()
#
# # for next 30000 key-value pair
#
# start5 = time.time()
# for i in range(50000,80000):
#     dict.insertElement(keys[i],values[i])
#
# end5 = time.time()
#
# # for last 20000 key-value pair
#
# start6 = time.time()
# for i in range(80000,len(keys)):
#     dict.insertElement(keys[i],values[i])
#
# end6 = time.time()


# print(end1 - start1)
# print(end2-start2)
# print(end3-start3)
# print(end4-start4)
# print(end5-start5)
# print(end6-start6)

# Analysis for Search

# value = []
# for i in range(0,1000):
#     val = dict.findElement(keys[i])
#     value = value.append(val)

# Analysis for Deletion

# 1. Removing 10,000 keys from a 100,000 SkipList

for i in range(0, 10000):
    dict.removeElement(keys[i])
