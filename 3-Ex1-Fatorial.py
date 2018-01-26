#Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

Numero = int(input("Digite o valor de n: "))

i = 1
Fator = 1

while i <= Numero:
	Fator = Fator * i
	i = i + 1
print (Fator)
