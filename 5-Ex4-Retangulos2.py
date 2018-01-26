#Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente.
#O programa deve imprimir retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = 0
y = 0

while x < altura:
    if x == 0 or x == altura-1:
        while y < largura:
            print("#", end="")
            y = y + 1
    else:
        while y <= largura:
            if y == 0 or y == largura:
                print("#", end="")
            else:
                while y+1 < largura:
                    print(" ", end="")
                    y = y + 1
            y = y + 1
    y = 0
    print()
    x = x + 1
