# https://olimpiada.ic.unicamp.br/pratique/p2/2018/f1/compensacao/
import sys

def read_numbers():
	return [int(x) for x in sys.stdin.readline().split()]


M, N = read_numbers()
net = [0] * (N+1)
total = 0
ans = ''
new_total = 0

for _ in range(M):
	X, W, Y = read_numbers()
	net[X] += W
	net[Y] -= W
	total += W

for n in net:
	if n > 0:
		new_total += n


ans = 'S' if new_total < total else 'N'
#print(new_total)
sys.stdout.write("%s\n%d\n" % (ans, new_total))
