#Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder, respectivamente, 
#às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, 
#respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos.
#Se a distância for maior ou igual a 10, imprima "longe" na saída.
#Caso o contrário, quando a distância for menor que 10, imprima "perto"

import math

x1 = int(input("Entre com o ponto X1: "))
y1 = int(input("Entre com o ponto Y1: "))
x2 = int(input("Entre com o ponto X2: "))
y2 = int(input("Entre com o ponto Y2: "))

distancia = math.sqrt(((x2 - x1)**2) + ((y2 -y1)**2))

if distancia >= 10:
   print ("longe")
else:
   print ("perto")