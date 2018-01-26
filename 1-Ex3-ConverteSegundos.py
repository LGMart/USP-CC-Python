#Faça um programa em Python que dada a quantidade de segundos, o programa "quebra" esse valor em dias, horas, minutos e segundos.
#A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

Entrada = input("Por favor, entre com o número de segundos que deseja converter: ")
TotalSegundos = int(Entrada)


Dias = TotalSegundos // 86400
Segundos_Restantes = TotalSegundos % 86400
Horas = Segundos_Restantes // 3600
Segundos_Restantes = Segundos_Restantes % 3600
Minutos = Segundos_Restantes // 60
Segundos = Segundos_Restantes % 60

print (Dias,"dias,",Horas,"horas,",Minutos,"minutos e",Segundos,"segundos.")
