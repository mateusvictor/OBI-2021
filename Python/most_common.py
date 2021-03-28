"""
	Algorithms to find the most common items in a list 
	1) Algorithm 1: Using sorted() function
		- delta time: 

	2) Algorithm 2: Using Counter().most_common()
		- delta time:
"""

ARR = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]

# 1) Using sorted()
from datetime import datetime

#philanthrope x kupla - cicles - BOM PA CARAIO

time1 = datetime.now()

unique = sorted(list(set(ARR)))

mylist = [(number, ARR.count(number)) for number in unique]
most_common = sorted(mylist, key=lambda x: x[1], reverse=True)

for item, counter in most_common:
	print(f"Item: {item:} [{counter} times]")

delta_time = (datetime.now() - time1).total_seconds()
print(f"Execution time (Algorithm 1): {delta_time} seconds\n\n")

# 2) Using  Counter().most_common()
from collections import Counter

time1 = datetime.now()

counter = Counter(ARR)
most_common = counter.most_common()

for item, counter in most_common:
	print(f"Item: {item} [{counter} times]")

delta_time = (datetime.now() - time1).total_seconds()
print(f"Execution time (Algorithm 1): {delta_time} seconds")
