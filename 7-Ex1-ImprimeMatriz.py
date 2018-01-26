# Escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro
#e imprime a matriz, linha por linha.

def imprime_matriz(matriz):
    i = 0
    j = 0
    qtd_colunas = len(matriz[0])
    qtd_linhas = len(matriz)
    while i < qtd_linhas:
        while j < qtd_colunas:
            if j == qtd_colunas - 1:
                print(matriz[i][j], end="")
            else:
                print(matriz[i][j], end=" ")
            j = j + 1
        print()
        j = 0
        i = i + 1


#matriz = [[1, 2, 3], [4, 5, 6]]
#imprime_matriz(matriz)
