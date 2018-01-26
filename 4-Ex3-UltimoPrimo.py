#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
#e retorna o maior número primo menor ou igual ao número passado à função

def check_primo(n):
   é_primo = True
   divisor = n -1

   while divisor > 1 and é_primo:
      if n % divisor == 0:
         é_primo = False
         return é_primo
      divisor = divisor - 1
   return é_primo


def maior_primo(m):

   while check_primo(m) != True:
      m = m -1
   return m

Numero = int(input("Digite um número inteiro: "))
print(maior_primo(Numero))
