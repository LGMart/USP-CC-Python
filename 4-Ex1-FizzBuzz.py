#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e retorna
#'Fizz' se o número for divisível por 3 e não for divisível por 5;
#'Buzz' se o número for divisível por 5 e não for divisível por 3;
#'FizzBuzz' se o número for divisível por 3 e por 5;
#Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve retornar o número recebido como parâmetro.

def fizzbuzz (Numero):

	if (Numero % 3) == 0 and (Numero % 5) != 0:
		return ("Fizz")
	elif (Numero % 5) == 0 and (Numero % 3) != 0:
		return ("Buzz")
	elif (Numero % 5) == 0 and (Numero % 3) == 0:
		return ("FizzBuzz")
	else:
		return (Numero)

Numero = int(input("Entre com um numero: "))
fizzbuzz(Numero)
