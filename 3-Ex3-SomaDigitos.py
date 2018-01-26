#Escreva um programa que receba um número inteiro na entrada, 
#calcule e imprima a soma dos dígitos deste número na saída

Entrada = input("Digite um número inteiro: ")
Tamanho = len(Entrada)
Numero = int(Entrada)

i = 0
Restante = Numero
Soma = 0


while i < Tamanho:
	Parte = Restante % 10
	Soma = Soma + Parte
	Restante = Restante // 10
	i += 1
print (Soma)
