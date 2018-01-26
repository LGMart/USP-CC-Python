#Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
#O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = 0
y = 0

while x < altura:
    while y < largura:
        print("#", end="")
        y = y + 1
    y = 0
    print()
    x = x + 1
