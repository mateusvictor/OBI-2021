# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/elevador/

# N = int(input())
# weights = sorted([int(n) for n in input().split()])

# base = 0
# ans = 'S'

# for w in weights:
# 	if w <= 8:
# 		base = max(base, w)
# 		continue

# 	elif w-base > 8:
# 		ans = 'N'
# 		break		

# 	base = w
	
# print(ans)

L = int(input())
C = int(input())
type2 = (L-1)*2 + (C-1)*2
type1 = L*C + (C-1)*(L-1)
print(type1)
print(type2)
