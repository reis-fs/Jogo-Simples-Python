#coding: utf-8
import random

#vida do jogador
vida_jogador = 100
#mana do jogador
mana_jogador = 100

#vida do inimigo
vida_inimigo = 50

#número de inimigos
n = int(input("Digite a quantidade de inimigos: "))

#verifica se a quantidade de inimigos é maior que zero
#se for menor que zero, o jogo exibirá uma mensagem de erro e será fechado
if n <= 0:
    print("Erro, a quantia de inimigos precisa ser maior que 0!")
    exit()

#vetor para armazenar os inimigos
inimigos =[]

#add ao vetor o indice do inimigo e sua vida
for i in range(n):
    inimigos.append([i+1, vida_inimigo])

#variável para rodar os loops
jogando = True
while jogando:
    print("Vida:", vida_jogador)
    print("Mana:", mana_jogador)
    print("")

    #jogador escolque o que fazer
    escolha = int(input("Deseja atacar (1) ou curar (2): "))
    print("")

    #se escolher atacar
    if escolha == 1:
        #escolhe um inimigo aleatoriamente para ser atacado
        selecionado = random.choice(inimigos)
        #determinar dano causado
        dano = random.randint(10, 15)

        #mostrara informações ao jogador
        print("Você causou %d de dano ao inimigo %d!" % (dano, selecionado[0]))

        #diminuir a vida do inimigo com o dano causado
        selecionado[1] -= dano

        #se o inimigo morrer
        if selecionado[1] <= 0:
            #mostrar o inimigo que morreu
            print("O inimigo %d morreu!" % selecionado[0])
            #remover da lista de inimigos
            inimigos.remove(selecionado)

    #se escolher curar
    elif escolha == 2:
        #cura só é possivel quando maior que dez
        if vida_jogador >= 10:
            #cura aleatória
            cura = random.randint(10, 15)
            #mostra o quanto foi curado
            print("Você recebeu %d de cura!" %cura)
            #adicionamor à vida do jogador
            vida_jogador += cura
            #diminuir a mana do jogador
            mana_jogador -= 10

        #se o jogador tiver menos de 10 de mana
        else:
            #mostramos ao jogador que não pode se curar
            print("Mana insuficiente!")

    #se o jogador escolher uma opção diferente de 1 e 2, o jogo exibe uma mensagem de erro e fecha
    else:
        print("Erro, escolha entre os valores 1 para atacar ou 2 para curar.")
        exit()

    #vez dos inimigos atacarem
    for inimigo in inimigos:
        #definimos a chance do inimigo acertar ou errar (acertar = 75% de chance)
        acertou = bool(random.choice([1, 1, 1, 0]))

        #se acertar
        if acertou:
            #definir o dano causado ao jogador
            dano = random.randint(1, 5)
            print("O inimigo %d causou %d de dano!" %(inimigo[0], dano))
            #diminuir a vida do jogador
            vida_jogador -= dano

        #se o inimigo errar
        else:
            print("O inimigo %d errou o ataque!" %inimigo[0])

    #aumentar a mana do jogador (3 a cada rodada)
    if mana_jogador < 100:
        mana_jogador += 3

    #define limite de mana
    if mana_jogador > 100:
        mana_jogador = 100

    #se a vida do jogador zerar ele perde
    if vida_jogador <= 0:
        print("Você perdeu o jogo!")
        jogando = False

    #se todos os inimigos morrerem ele ganha
    if len(inimigos) == 0:
        print("Todos os inimigos morreram, você ganhou o jogo!")
        jogando = False
