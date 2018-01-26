# Ler uma sequencia de numeros inteiros terminada por zero
# apos ZERO, imprimir a sequencia em ordem inversa

lista=[]
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    lista.append(num)

tam = len(lista) - 2
while tam >= 0:
    print(lista[tam])
    tam = tam - 1
