# Python
Jogo de ataque e cura feito em Python

Neste jogo simples, o jogador precisa eliminar a quantidade de inimigos que for digitado por ele.
Toda rodada será mostrada sua vida e sua mana.

O jogador terá duas escolhas, atacar(1) ou curar(2).
Se a escolhar for atacar, será selecionado um inimigo aleatório e causará um dano aleatório à ele numa escala de 10~15.
Se a escolha for curar, será verificado se o jogador tem mana o suficiente (curar custa 10 de mana) e irá realizar a cura num valor aleatório entre 10~15.
Depois da escolha do jogador, será a vez dos inimigos atacarem. 
O jogo percorrerá cada um dos inimigos apontando o dano que cada um causou ao jogador. O dano dos inimigos variam entre 1~5 e também é escolhido de forma aleatória. Porém, existe 25% de chance do inimigo errar o ataque.
No final de cada rodada o jogador recebe 3 de mana e o limite de mana é 100.
O jogo acaba quando o jogador eliminar todos os inimigos ou morrer.
