def computador_escolhe_jogada(n,m):
    jogada = 1
    if m >= n or n == 1:
        jogada = n
#    elif n % (m+1) == 0:
#        jogada = m        
    elif m < n:
        aux = m
        while (n-aux) % (m+1) != 0:
            if aux > 1:
                aux = aux - 1
            else:
                aux = m
                break
        jogada = aux
    else:
        jogada = m
    if jogada == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou ",jogada,"peças.")
    n = n - jogada
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n > 1:
        print("Agora restam",n,"peças no tabuleiro.") 
    return jogada

def usuario_escolhe_jogada(n,m):
    vencedor_jogador = 0
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada > n or jogada <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    if jogada == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",jogada,"peças.")
    n = n - jogada
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n > 1:
        print("Agora restam",n,"peças no tabuleiro.")
    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m > n or m < 1:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    if m == 1 and n % 2 !=0:
        print("Computador começa!")
        while n > 0:
            jogada = computador_escolhe_jogada(n,m)
            n = n - jogada
            vencedor = "computador"
            vitoria_computador = 1
            if n > 0:
                jogada = usuario_escolhe_jogada(n,m)
                n = n - jogada
                vencedor = "usuario"
                vitoria_usuario = 1
                
    elif m == 1 and n % 2 ==0:
        print("Voce começa!")
        while n > 0:
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            vencedor = "usuario"
            vitoria_usuario = 1
            if n > 0:
                jogada = computador_escolhe_jogada(n,m)
                n = n - jogada
                vencedor = "computador"
                vitoria_computador = 1
                
    elif (n % (m-1)) == 0 and m > 1 and m < n:
        print("Voce começa!")
        while n > 0:
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            vencedor = "usuario"
            vitoria_usuario = 1
            if n > 0:
                jogada = computador_escolhe_jogada(n,m)
                n = n - jogada
                vencedor = "computador"
                vitoria_computador = 1
    else:
        print("Computador começa!")
        while n > 0:
            jogada = computador_escolhe_jogada(n,m)
            n = n - jogada
            vencedor = "computador"
            vitoria_computador = 1
            if n > 0:
                jogada = usuario_escolhe_jogada(n,m)
                n = n - jogada
                vencedor = "usuario"
                vitoria_usuario = 1

    if n == 0:
        print ("Fim do jogo! O",vencedor,"ganhou!")
    return vencedor

def campeonato():
    rodada = 0
    pontos_computador = 0
    pontos_usuario = 0
    vitoria_computador = 0
    vitoria_usuario = 0
    while rodada < 3:
        print("**** Rodada ",rodada+1," ****")
        if partida() == "computador":
            pontos_computador = pontos_computador + 1
        else:
            pontos_usuario = pontos_usuario + 1
        rodada = rodada + 1
    print("Placar: Você ",pontos_usuario," X ",pontos_computador," Computador")

# INICIO DO PROGRAMA
escolha = 0

while escolha not in (1,2):
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))

if escolha == 1:
    print ("Voce escolheu uma partida isolada!")
    partida()
elif escolha == 2:
    print ("Voce escolheu um campeonato!")
    campeonato()


