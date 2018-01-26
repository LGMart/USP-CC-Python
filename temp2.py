import re
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

def limpa_texto(lista_texto):
    lista_limpa = []
    for i in range(len(lista_texto)):
        clean = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ\-\(\)\[\]\"\{\} ]', '', lista_texto[i])
        lista_limpa.append(clean)
    return lista_limpa


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

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

        
#    palavras_limpa = limpa_texto(texto.split())    
    palavras_unicas = n_palavras_unicas(lista_palavras2)
    palavras_diferentes = n_palavras_diferentes(lista_palavras2)

    wal = soma_carac_palavra / conta_palavras
    ttr = palavras_diferentes / conta_palavras
    hlr = palavras_unicas / conta_palavras
    sal = soma_carac_sentenca / conta_sentenca
    sac = conta_frases / conta_sentenca
    pal = soma_carac_frase / conta_frases

    print("PALAVRAS = ",conta_palavras)
    print("conta_carac_palavras = ",soma_carac_palavra)
    print("FRASES = ",conta_frases)
    print("conta_carac_frase",soma_carac_frase)
    print("SENTENCAS = ",conta_sentenca)
    print("soma carac sentenca = ",soma_carac_sentenca)
    print("PALAVRAS UNICAS",palavras_diferentes)
    print("PALAVRAS DIFERENTES",palavras_unicas)
    print()
    print("wal = ",wal)
    print("ttr = ",ttr)
    print("hlr = ",hlr)
    print("sal = ",sal)
    print("sac = ",sac)
    print("pal = ",pal)



#    wal = #tamanho medio de palavra = soma dos tamanhos das palavras dividida pelo número total de palavras = soma len(lista[x])/len(lista)
#    ttr = #relação Type-Token = soma do número de palavras únicas dividida pelo número total de palavras. = 
#    hlr = #Razão Hapax Legomana = soma do número de palavras que aparecem uma única vez dividida pelo total de palavras
#    sal = #tamanho médio de sentença = soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
#    sac = #complexidade média da sentença =  número total de frases divido pelo número de sentenças
#    pal = #tamanho medio de frase = soma do número de caracteres em cada frase dividida pelo número de frases no texto


texto0 = "O gato caçava o rato" 
texto = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
texto3 = "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."


calcula_assinatura(texto3)
