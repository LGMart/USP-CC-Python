#Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido 
#possui ao menos um dígito com um dígito adjacente igual a ele.
#Caso exista, imprima "sim". Se não existir, imprima "não".

Entrada = input("Digite um número inteiro: ")
Tamanho = len(Entrada)
Numero = int(Entrada)

i = 1
Restante = Numero
AcheiDigito = False

while i < Tamanho and AcheiDigito != True:
	Digito1 = Restante % 10
	Restante = Restante // 10
	Digito2 = Restante % 10
	i += 1
	if Digito1 == Digito2:
		print ("sim")
		AcheiDigito = True
if AcheiDigito == False or Tamanho == 1:
		print ("nao")
