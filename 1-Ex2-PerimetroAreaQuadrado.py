#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
#calcule e imprima (saída de dados) seu perímetro e sua área.

lado = input("Digite o valor correspondente ao lado de um quadrado: ")

area = int(lado) ** 2
perimetro = int(lado) * 4

print ("perímetro:",perimetro,"- área:",area)