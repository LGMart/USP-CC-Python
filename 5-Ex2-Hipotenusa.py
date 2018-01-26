#Escreva uma função 'soma_hipotenusas' que receba como parâmetro
#um número inteiro positivo e retorna a soma de todos os inteiros
#entre 1 e n que são comprimento da hipotenusa de algum triângulo
#retângulo com catetos inteiros.

import math

def soma_hipotenusas(max_c): #Testa
    a = 1
    b = 1
    c = 1
    soma_hip = 0
    while c <= max_c:
        while a < max_c:
            while b < max_c:
                if c**2 == (a**2 + b**2):
#                    print("ACHEI a=",a,"b=",b,"hip",c,)
                    soma_hip = soma_hip + c
                b = b + 1
            b = 1
            a = a + 1
        a = 1
        c = c + 1
    soma_hip = soma_hip/2
    return soma_hip

#main
numero = int(input("Digite um numero intero: "))
print(int(soma_hipotenusas(numero)))
