#Escreva a função vogal que recebe um único caractere como parâmetro e 
#retorna True se ele for uma vogal e False se for uma consoante.

def vogal(x):
    vogais = ["A","E","I","O","U","a","e","i","o","u"]
    check = True
    if x in vogais:
        check = True
    else:
        check = False
    return check

letra = input("Digite uma letra: ")
print(vogal(letra))
