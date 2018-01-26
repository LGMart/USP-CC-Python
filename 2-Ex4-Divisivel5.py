#Receba um número inteiro na entrada e imprima
# "Buzz" se o número for divisível por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

Numero = int(input("Entre com o número "))

if (Numero % 5) == 0:
	print ("Buzz")
else:
	print(Numero)