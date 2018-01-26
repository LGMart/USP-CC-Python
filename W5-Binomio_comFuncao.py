def Fatorial (Numero):
	i = 1
	Fator = 1
	while i <= Numero:
		Fator = Fator * i
		i = i + 1
	return (Fator)

def numero_binomial (n,k):
        return Fatorial(n) / (Fatorial(k) * Fatorial(n-k))

# n = int(input("Digite o valor de n: "))
# k = int(input("Digite o valor de n: "))


