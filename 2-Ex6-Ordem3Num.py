#Receba 3 números inteiros na entrada e imprima
# "crescente" se eles forem dados em ordem crescente.
# Caso contrário, imprima "não está em ordem crescente"

Primeiro = int(input("Entre com o primeiro número "))
Segundo = int(input("Entre com o segundo número "))
Terceiro = int(input("Entre com o terceiro número "))

if Primeiro < Segundo < Terceiro:
	print ("crescente")
else:
	print("não está em ordem crescente")