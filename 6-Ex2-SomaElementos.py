# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros
#e retorna um número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma


lista=[]
num = 1
while num != 0:
    num = int(input("Digite uma sequencia de numeros a ser somada, 0 para terminar: "))
    lista.append(num)
print (soma_elementos(lista))
