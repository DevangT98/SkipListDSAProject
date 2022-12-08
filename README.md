Prerequisites : 
• For easy evaluation, VSCode or PyCharm IDE is suggested. 
• We have used NumPy module to analyze performance. 
• To install NumPy on PyCharm, click on File and go to the settings. Under Settings, 
choose your Python project and select Python Interpreter. Then, search for the NumPy 
package and click Install Package.
To evaluate implementation : 
• Open SkipListTest.py file and run it.
To evaluate performance :
• Open performanceAnalyzer.py file and run it. It would run for around 5-7 mins and will 
output performance numbers. 
• First, we have inserted 500,000 key-value pair and then five insertions of 200,000 pair 
up to total 1.5 million key-value pair.
• For Search, ClosestKeyBefore and ClosestKeyAfter Operation, we have tested with 
10,000 operations with equal number of successful and unsuccessful searches.
• For Deletion, we are clearing SkipList one by one, in the batch of 200,000 removal and 
till all out.