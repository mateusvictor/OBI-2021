# https://noic.com.br/materiais-informatica/problemas-da-semana/intermediario-semana24/

counter = 1

while True:
	J = int(input())

	if J == 0:
		break

	scores = []
	final = {}

	for player in range(J):
		player = str(input())
		scores = sorted([int(n) for n in input().split()])
		del scores[0], scores[-1]

		final[player] = sum(scores)

	final = sorted(final.items())
	final = sorted(final, key=lambda x: x[1], reverse=True)
		
	if counter != 1:
		print('')

	print(f"Teste {counter}")

	for i, item in enumerate(final):
		print(f'{i+1} {item[0]} {item[1]}')

	counter += 1
