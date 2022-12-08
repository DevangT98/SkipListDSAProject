'''
   Author: Ravi Varadarajan
   Date created: 11/8/2022
'''
from OrderedDictionary import OrderedDictionary, DictionaryException
from SkipList1 import SkipList


def getOption():
    option = 0
    while True:
        print('Enter one of the following options:')
        print('(1 -- Insert, 2 -- Delete, 3 --- Find, 4 --- ClosestkeyAfter,'
              '5 --- ClosestkeyBefore, 6 --- Display, 7 --- Exit):')
        try:
            option = int(input())
            if option >= 1 and option <= 7:
                return option
        except:
            continue


def testIntKeyIntValues(dict):
    while True:
        option = getOption()
        if option == 1:
            # insert operation
            st = input(
                'Enter integer key and value to be inserted separated by space:')
            lst = st.split()
            key = int(lst[0])
            val = int(lst[1])
            oldVal = dict.insertElement(key, val)
            print('Old value = {}'.format(oldVal))
        elif option == 2:
            # delete operation
            key = int(input('Enter integer key to be removed: '))
            try:
                val = dict.removeElement(key)
                print('Value for key removed = {}'.format(val.value))
            except DictionaryException:
                print('Key {} does not exist'.format(key))
        elif option == 3:
            # find operation
            key = int(input('Enter integer key to look up: '))
            val = dict.findElement(key)
            if val.value == None or val.value == SkipList.negative_inf or val.value == SkipList.positive_inf:
                print('Key {} not found'.format(key))
            else:
                print('Value for key {} = {}'.format(key, val.value))
        elif option == 4:
            # closestKeyAfter operation
            key = int(input('Enter integer key to look up: '))
            key1 = dict.closestKeyAfter(key)
            if key1 == None:
                print('Given key {} exceeds the largest in the dictionary'.format(key))
            else:
                print('Closest key after key {} = {}'.format(key, key1.key))
        elif option == 5:
            # closestKeyBefore operation
            key = int(input('Enter integer key to look up: '))
            key1 = dict.closestKeyBefore(key)
           # print(f"Value of key1 retuned after closest key before : {key1}")
            if key1 == None or key1 == SkipList.negative_inf:
                print('Given key {} is below the smallest in the dictionary'.format(key))
            else:
                print('Closest key before key {} = {}'.format(key, key1))
        elif option == 7:
            # exit
            quit()
        dict.display()
        dict.size()


testIntKeyIntValues(SkipList())
