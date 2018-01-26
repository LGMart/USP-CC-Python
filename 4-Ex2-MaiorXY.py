#Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo (x, y):
    return max (x,y)
#    if x > y:
#        return x
#    else:
#        x = y
#        return x

x = int(input("Insira o primeiro número (x): "))
y = int(input("Insira o segundo número (y): "))
print(maximo (x, y))
