'''
   Author: Ravi Varadarajan
   Date created: 11/8/2022
'''


class DictionaryException(Exception):
    pass


class OrderedDictionary:

    '''
       Insert/replace value associated with key
       Return the previous value for the key if it already exists, else null
    '''
    def insertElement(k, v):
        pass

    '''
       Remove key and value associated with the key
       Return old value associated with the key or None if it does not exist
       Throws DictionaryException if key does not exist
    '''

    def removeElement(self, k):
        pass

    '''
       Return value associated with the key or None if key does not exist
    '''

    def findElement(self, k):
        pass

    '''
      Get the smallest key greater than or equal to the given key in the dictionary or
      return None if the given key exceeds the largest key in the dictionary
    '''

    def closestKeyAfter(self, k):
        pass

    '''
      Get the largest key smaller than or equal to the given key in the dictionary or
      return None if the given key is below the smallest key in the dictionary
    '''

    def closestKeyBefore(self, k):
        pass

    '''
       Return number of keys in the dictionary
    '''

    def size(self) -> int:
        pass

    '''
        Display the data structure
    '''

    def display(self):
        pass
