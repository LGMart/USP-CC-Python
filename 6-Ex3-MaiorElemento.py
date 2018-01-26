#Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros
#e retorna um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):
    maximo = max(lista)
    return maximo

lista = []
num = 1
while num !=0:
    num = int(input("Digite uma sequencia de numeros a ser somada, 0 para terminar: "))
    lista.append(num)
print(maior_elemento(lista))
