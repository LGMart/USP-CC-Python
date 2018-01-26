# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro
# e imprime as dimensões da matrix recebida, no formato iXj.

def dimensoes(matriz):
    qtd_colunas = len(matriz[0])
    qtd_linhas = len(matriz)
    print(qtd_linhas,"X",qtd_colunas, sep="")


#minha_matriz = [[1, 2, 3], [4, 5, 6]]
#dimensoes(minha_matriz)
#minha_matriz = [[1], [2], [3]]
#dimensoes(minha_matriz)
