def cria_matriz(num_linhas, num_colunas):
        matriz = []	#lista vazia
        for i in range(num_linhas):
                #cria a linha i
                linha = []	#lista vazia
                for j in range(num_colunas):
                        valor = int(input("Digite o valor de [" + str(i) + "][" + str(j) + "]"))
                        linha.append(valor)
                # adiciona linha à matriz
                matriz.append(linha)
        return matriz

def le_matriz():
        lin = int(input("Digite o numero de linhas da matriz: "))
        col = int(input("Digite o numero de colunas da matriz: "))
        matriz = cria_matriz(lin,col)
        return matriz

# imprimir em formato de matriz
matriz = le_matriz()
tamanho = len(matriz)-1
for linha in matriz:
        print(linha)
