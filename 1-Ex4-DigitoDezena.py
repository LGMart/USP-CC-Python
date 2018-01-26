#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

Numero = input("Digite um número inteiro: ")
IntNumero = int(Numero)


DezMilhares = IntNumero // 10000
RestoNumero = IntNumero % 10000

Milhares = RestoNumero // 1000
RestoNumero = RestoNumero % 1000

Centenas = RestoNumero // 100
RestoNumero = RestoNumero % 100

Dezenas = RestoNumero // 10
Unidades = RestoNumero % 10

print ("O dígito das dezenas é",Dezenas)
