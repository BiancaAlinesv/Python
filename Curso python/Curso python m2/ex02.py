from random import randint      
itens = ("Pedra", "Papel", "Tesoura")
computador = randint (0, 2)
print('''Suas Opçoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é sua jogada?"))
print("O computador escolheu {}" .format(itens[computador]))
print("O jogador jogou {}" .format(itens[jogador]))