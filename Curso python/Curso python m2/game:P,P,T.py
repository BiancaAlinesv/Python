from random import randint      
itens = ("Pedra", "Papel", "Tesoura")
computador = randint (0, 2)
print('''Suas Opçoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é sua jogada?"))
print("=" * 10)
print("O computador escolheu {}" .format(itens[computador]))
print("O jogador jogou {}" .format(itens[jogador]))
print("=" * 10)
if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("Jogada invalida!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("Jogada invalida!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("Jogada invalida!")