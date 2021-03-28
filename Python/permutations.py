from itertools import permutations
from datetime import datetime
perm = permutations(['m', 'a', 't', 'e', 'u', 'u', 's'], 3)

a = datetime.now()

for item in list(perm):
	print(item)

print((datetime.now() - a).total_seconds())
