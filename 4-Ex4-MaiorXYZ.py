#Escreva a função 'maximo' que recebe 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo (x, y, z):
    return max (x,y,z)

x = int(input("Insira o primeiro número (x): "))
y = int(input("Insira o segundo número (y): "))
z = int(input("Insira o terceiro número (z): "))
print(maximo (x, y, z))
