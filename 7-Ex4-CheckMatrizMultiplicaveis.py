# Duas matrizes são multiplicáveis se o número de colunas da primeira
# é igual ao número de linhas da segunda.
# Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro
# e retorna True se as matrizes forem multiplicavéis e False caso contrário.

def sao_multiplicaveis(m1, m2):
    SaoMultiplicaveis = False
    qtd_colunas_m1 = len(m1[0])
    qtd_linhas_m2 = len(m2)
    if qtd_colunas_m1 == qtd_linhas_m2:
        SaoMultiplicaveis = True
    return SaoMultiplicaveis


#m1 = [[1, 2, 3], [4, 5, 6]]
#m2 = [[2, 3, 4], [5, 6, 7]]
#print(sao_multiplicaveis(m1, m2))

#m1 = [[1], [2], [3]]
#m2 = [[1, 2, 3]]
#print(sao_multiplicaveis(m1, m2))
