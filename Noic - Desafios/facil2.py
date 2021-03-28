# https://noic.com.br/materiais-informatica/problemas-da-semana/iniciante-semana3/

N, x = [int(n) for n in input().split()]
people = [int(n) for n in input().split()]

people.sort(reverse=True)
print(people)
lista = []
p = 0
while p < len(people):
	if p == len(people)-1:
		lista.append([people[p]])
		break

	p1, p2 = people[p], people[p+1]

	if p1 + p2 <= x:
		lista.append([p1, p2])
		p += 1
	else:
		lista.append([p1])
	p += 1
print(lista)
print(len(lista))