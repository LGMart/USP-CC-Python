#Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro
#e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def n_primos(x):
    divisor = 2
    qtd = 0
    incremento = 2    
    while incremento <= x:
        é_primo = True
        while divisor < incremento and é_primo:
            if incremento % divisor == 0:
                é_primo = False
            divisor = divisor + 1
        incremento = incremento + 1
        divisor = 2
        if é_primo:
            qtd = qtd + 1
    return qtd


Numero = int(input("Digite um número inteiro >= 2: "))
print(n_primos(Numero))
