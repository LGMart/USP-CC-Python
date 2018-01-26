import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # pegar os elementos de 1 a 6 das duas listas, calcular a diferença, somar tudo, dividir por 6 e devolver o resultado. 
    # Fazer o módulo da diferença, pois em alguma das subtrações o resultado pode ser negativo.

    as_resultante = []
    soma = 0
    for i in range(6):
        diferenca =  as_a[i] - as_b[i]
        soma = soma + abs(diferenca)        
        as_resultante.append(diferenca)
    ratio = soma / 6
    return ratio
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

#    wal = #tamanho medio de palavra = soma dos tamanhos das palavras dividida pelo número total de palavras = soma len(lista[x])/len(lista)
#    ttr = #relação Type-Token = soma do número de palavras únicas dividida pelo número total de palavras. = 
#    hlr = #Razão Hapax Legomana = soma do número de palavras que aparecem uma única vez dividida pelo total de palavras
#    sal = #tamanho médio de sentença = soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
#    sac = #complexidade média da sentença =  número total de frases divido pelo número de sentenças
#    pal = #tamanho medio de frase = soma do número de caracteres em cada frase dividida pelo número de frases no texto
    

    lista_sentencas = separa_sentencas(texto)      # Cria lista de sentencas
    conta_sentenca = len(lista_sentencas)
    soma_carac_sentenca = 0
    for k in lista_sentencas:
        soma_carac_sentenca = soma_carac_sentenca + len(k)

    lista_frases = []                             # Cria lista de frases
    conta_frases = 0
    soma_carac_frase = 0
    for i in lista_sentencas:
        parte_frase = separa_frases(i)
        conta_frases = conta_frases + len(parte_frase)
        lista_frases.append(parte_frase)              #Sem append fica apenas ultima frase
        for k in parte_frase:
            soma_carac_frase = soma_carac_frase + len(k)

    lista_palavras = []
    conta_palavras = 0
    soma_carac_palavra = 0
    for i in lista_frases:
        for j in i:
            parte_palavra = separa_palavras(j)
            conta_palavras = conta_palavras + len(parte_palavra)
            lista_palavras.append(parte_palavra)
            for k in parte_palavra:
                soma_carac_palavra = soma_carac_palavra + len(k)
        
    lista_palavras2 = []        
    for i in lista_palavras:
        lista_palavras2 = lista_palavras2 + i  
    palavras_unicas = n_palavras_unicas(lista_palavras2)
    palavras_diferentes = n_palavras_diferentes(lista_palavras2)

    wal = soma_carac_palavra / conta_palavras
    ttr = palavras_diferentes / conta_palavras
    hlr = palavras_unicas / conta_palavras
    sal = soma_carac_sentenca / conta_sentenca
    sac = conta_frases / conta_sentenca
    pal = soma_carac_frase / conta_frases

    return [wal, ttr, hlr, sal, sac, pal]
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
        
    lista_assinaturas = []
    for i in textos:
        assinatura = []
        assinatura = calcula_assinatura(i)
        lista_assinaturas.append(assinatura)

        
    lista_comparada = []
    for i in range(len(lista_assinaturas)):
        comp = compara_assinatura(ass_cp, lista_assinaturas[i])
        lista_comparada.append(comp)

    j = lista_comparada[i]
    infectado = 0
    for i in range(len(lista_comparada)):
        if lista_comparada[i] < j:
            infectado = i
        else:
            i = i + 1

    return infectado
        
    
#avalia_textos recebe uma lista de textos e uma assinatura;
#para cada texto, você precisa calcular a assinatura, ou seja, você precisa chamar calcula_assinatura.
#Depois de ter a assinatura de todos os textos, você vai usar compara_assinaturas para descobrir qual dos textos
#tem a assinatura mais parecida com a assinatura recebida pela função.
# A partir do que a função avalia_textos devolve, você imprime a frase "O autor do texto X...".
    pass

def limpa_texto(lista_texto):
    lista_limpa = []
    for i in range(len(lista_texto)):
        clean = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ\-\(\) ]', '', lista_texto[i])
        lista_limpa.append(clean)
    return lista_limpa

assinatura = le_assinatura()
lista_texto = le_textos()
lista_limpa = limpa_texto(lista_texto)
infectado = 0
infectado = avalia_textos(lista_limpa,assinatura)

print("O autor do texto",infectado,"esta infectado com COH-PIAH")
