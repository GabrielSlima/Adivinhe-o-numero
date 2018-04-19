import random
numeroSecreto =  random.randint(1,20)
print('O numero que estou pensando esta entre 1 e 20')

#Dando ao usuario 6 oportunidades
for tentativa in range (1,7):
	print('Tente adivinhar:')
	numero = int(input())
	if numero < numeroSecreto:
		print('Seu numero está abaixo...')
	elif numero > numeroSecreto: 
		print('Seu numero está acima...')
	else:
		break
if numero == numeroSecreto:
	print('Parabens!!! O numero que pensei foi: ' + str(numeroSecreto) + '.')
else: 
	print('Você falhou soldado. O numero que pensei foi: ' + str(numeroSecreto) + '.')
