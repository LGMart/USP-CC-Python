#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
#Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Numero = int(input("Digite um número inteiro: "))

é_primo = True
divisor = 2

while divisor < Numero and é_primo:
	if Numero % divisor == 0:
		é_primo = False
	divisor += 1

if é_primo and Numero != 1:
	print("primo")
else:
	print("não primo")