#Escreva um programa que receba (entrada de dados através do teclado)
#o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura
#e imprima (saída de dados) a mensagem com os dados recebidos

NomeCliente = input("Digite o nome do cliente: ")
DiaVencimento = input("Digite o dia de vencimento: ")
MesVencimento = input("Digite o mês de vencimento: ")
ValorFatura = input("Digite o valor da fatura: ")

print ("Olá,",NomeCliente)
print ("A sua fatura com vencimento em",DiaVencimento,"de",MesVencimento,"no valor de R$",ValorFatura,"está fechada." )