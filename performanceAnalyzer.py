from SkipList1 import SkipList
import time
import numpy as np
import random

# Here we hold values of keys & values into an array from 0 to 500,000
keys = np.arange(0, 500000)
values = np.arange(0, 500000)

# Shuffling the above array so it mimics the real-world insertion
random.shuffle(keys)
random.shuffle(values)

dict = SkipList()

# Initially populating our SkipList with 500,000 key-value pairs
start1 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end1 = time.time()

# Now inserting 200,000 more key-value pair to the existing SkipList
# Here, we are inserting just even numbers, so that when we test for unsuccessful Search, ClosestKeyBefore
# & ClosestKeyAfter Operations with integers.

keys = np.arange(500000, 900000, 2)
values = np.arange(500000, 900000, 2)

random.shuffle(keys)
random.shuffle(values)

start2 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end2 = time.time()

# Now inserting another 200,000 key-value pairs to the existing SkipList

keys = np.arange(900000, 1100000)
values = np.arange(900000, 1100000)

random.shuffle(keys)
random.shuffle(values)

start3 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end3 = time.time()

# Now inserting another 200,000 key-value pairs to the existing SkipList

keys = np.arange(1100000, 1300000)
values = np.arange(1100000, 1300000)

random.shuffle(keys)
random.shuffle(values)

start4 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end4 = time.time()

# Now inserting another 200,000 key-value pairs to the existing SkipList

keys = np.arange(1300000, 1500000)
values = np.arange(1300000, 1500000)

random.shuffle(keys)
random.shuffle(values)

start5 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end5 = time.time()

# Now inserting another 200,000 key-value pairs to the existing SkipList

keys = np.arange(1500000, 1700000)
values = np.arange(1500000, 1700000)

random.shuffle(keys)
random.shuffle(values)

start6 = time.time()
for i in range(0, len(keys)):
    dict.insertElement(keys[i], values[i])
end6 = time.time()

After_Total_insertion = dict.size()

# Analyzing Search Operation

# In our SkipList, from 500,000 to 900,000 key, we have even numbers only.
# So, searching from the above range, we will have equal number of successful and unsuccessful operations.

start13 = time.time()
for i in range(0, 100000):
    x = random.randrange(500000, 900000)
    dict.findElement(x)
end13 = time.time()

# Analyzing ClosestKeyBefore Operation

# In our SkipList, from 500,000 to 900,000 key, we have even numbers only. So, searching the closestKeyBefore from
# the above range, we will have equal number of successful and unsuccessful operations.

start14 = time.time()
for i in range(0, 100000):
    x = random.randrange(500000, 900000)
    dict.closestKeyBefore(x)
end14 = time.time()

# Analyzing ClosestKeyAfter Operation

# In our SkipList, from 500,000 to 900,000 key, we have even numbers only. So, searching the closestKeyAfter from
# the above range, we will have equal number of successful and unsuccessful operations.

start15 = time.time()
for i in range(0, 100000):
    x = random.randrange(500000, 900000)
    dict.closestKeyAfter(x)
end15 = time.time()

# Analysing Deletion

start7 = time.time()
for i in range(0, 200000):
    dict.removeElement(i)
end7 = time.time()

start8 = time.time()
for i in range(200000, 400000):
    dict.removeElement(i)
end8 = time.time()

start9 = time.time()
for i in range(500000, 900000, 2):
    dict.removeElement(i)
end9 = time.time()

start10 = time.time()
for i in range(900000, 1100000):
    dict.removeElement(i)
end10 = time.time()

start11 = time.time()
for i in range(1100000, 1300000):
    dict.removeElement(i)
end11 = time.time()

for i in range(1300000, 1700000):
    dict.removeElement(i)
for i in range(400000, 500000):
    dict.removeElement(i)

end12 = time.time()
After_Total_Deletion = dict.size()

print('-------------------------- Final Statements--------------------------------\n\n')

# Printing time for each insertion & its average
print('Insertion\n')

print(
    f'The first insertion of 500,000 key-value pair takes {end1 - start1} seconds')
print(
    f'The second insertion of 200,000 key-value pair takes {end2 - start2} seconds')
print(
    f'The third insertion of 200,000 key-value pair takes {end3 - start3} seconds')
print(
    f'The fourth insertion of 200,000 key-value pair takes {end4 - start4} seconds')
print(
    f'The fifth insertion of 200,000 key-value pair takes {end5 - start5} seconds')
print(
    f'The sixth insertion of 200,000 key-value pair takes {end6 - start6} seconds\n')

avg_insertion = ((end2 - start2) + (end3 - start3) +
                 (end4 - start4) + (end5 - start5) + (end6 - start6)) / 5
print(
    f'The Average Insertion time after 500,000 size SkipList is {avg_insertion} seconds for every 200,000 pairs')

print(f'Size of SkipList After Every Insertion : {After_Total_insertion}\n\n')

# Printing time taken to search for an equal No. of Successful and Unsuccessful searches.
print('Search Operation\n')

print(f'Time taken for 100,000 search operations : {end13-start13} seconds')
avg_search = ((end13-start13)/100000)
print('Average Search Operation takes in a 1.5 Million size SkipList is :' +
      "{:f}".format(avg_search)+' seconds\n\n')

# Printing time taken to search Closest Key Before a given element for a equal No. of Successful and Unsuccessful
# searches.
print('ClosestKeyBefore Operation\n')

print(
    f'Time taken for 100,000 ClosestKeyBefore operations : {end14-start14} seconds')
avg_ckb = ((end14-start14)/100000)
print('Average ClosestKeyBefore Operation takes in a 1.5 Million size SkipList is :' +
      "{:f}".format(avg_ckb)+' seconds\n\n')

# Printing time taken to search Closest Key After a given element for a equal No. of Successful and Unsuccessful
# searches.
print('ClosestKeyAfter Operation\n')

print(
    f'Time taken for 100,000 ClosestKeyAfter operations : {end15-start15} seconds')
avg_cka = ((end15-start15)/100000)
print('Average ClosestKeyAfter Operation takes in a 1.5 Million size SkipList is :' +
      "{:f}".format(avg_cka)+' seconds\n\n')


# Printing time for deletion of every 200,000 pairs and clearing SkipList
print('Deletion\n')

print(
    f'The first deletion of 200,000 key-value pair from 1.5 Million size SkipList takes {end7 - start7} seconds')
print(
    f'The second deletion of 200,000 key-value pair from 1.3 Million size SkipList takes {end8 - start8} seconds')
print(
    f'The third deletion of 200,000 key-value pair from 1.1 Million size SkipList takes {end9 - start9} seconds')
print(
    f'The fourth deletion of 200,000 key-value pair from 0.9 Million size SkipList takes {end10 - start10} seconds')
print(
    f'The fifth deletion of 200,000 key-value pair from 0.7 Million size SkipList takes {end11 - start11} seconds\n')

avg_deletion = ((end7 - start7) + (end8 - start8) +
                (end9 - start9) + (end10 - start10) + (end11 - start11)) / 5
total_deletion = end12 - start7

print(
    f'The Average Deletion time taken from a 1.5 Million size SkipList is : {avg_deletion} seconds for every 200,000 pairs')
print(
    f'The total time taken to Delete a 1.5 Million size Skiplist is : {total_deletion} seconds')

print(f'Size of SkipList After All Deletion : {After_Total_Deletion}\n\n')
