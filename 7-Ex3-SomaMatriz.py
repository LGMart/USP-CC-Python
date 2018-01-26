#Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes
# e retorna uma matriz que represente sua soma caso as matrizes tenham dimensões iguais.
# Caso contrário, a função deve retornar False.

def Check_matriz(matriz1, matriz2):
    MatrizIguais = True
    qtd_colunas_m1 = len(matriz1[0])
    qtd_linhas_m1 = len(matriz1)
    qtd_colunas_m2 = len(matriz2[0])
    qtd_linhas_m2 = len(matriz2)
    if qtd_colunas_m1 != qtd_colunas_m2 or qtd_linhas_m1 != qtd_linhas_m2:
        MatrizIguais = False
    return MatrizIguais

def soma_matrizes(m1, m2):
    check = Check_matriz(m1, m2)
    if check == False:
        return check
    else:
        m3 = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                valor =  m1[i][j] + m2[i][j]
                linha.append(valor)
            m3.append(linha)
        return m3


#m1 = [[1], [2], [3]]
#m2 = [[2, 3, 4], [5, 6, 7]]
#print(soma_matrizes(m1, m2))

m1 = [[1,2], [3,4]]
m2 = [[2, 3, 4], [5, 6, 7], [8, 9, 0]]
print(soma_matrizes(m1, m2))
