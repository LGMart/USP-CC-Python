# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
# verifica se tal lista possui elementos repetidos e os remove.
# A função deve retornar uma lista correspondente à primeira lista, sem elementos repetidos.
# A lista retornada deve estar ordenada.

def remove_repetidos(lista):
    lista.sort()
    for x in range(len(lista)):
        if x == len(lista)-1:
            break
        else:
            while lista[x] == lista[x+1]:
                del lista[x]
    return lista


lista = []
num = 1
while num != 0:
    num = int(input("Digite um número. 0 para sair: "))
    lista.append(num)
zero = len(lista)-1
del lista[zero]
print(remove_repetidos(lista))
