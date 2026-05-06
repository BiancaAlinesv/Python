
velocidade= int(input("Qual a velocidade do veiculo? "))
multa= (velocidade - 80) * 7
if velocidade > 80:
    print("Voce ultrapassou o limite de velocidade, foi multado!")
    print("Sua multa é de R${:.2f}! " .format(multa))
else: 
    print("Pode seguir ")

number= int(input("Digite um numero inteiro: "))
resultado= number % 2
if resultado == 0:
    print("Seu numero {} é par" .format(number))
else:
    print("Seu numero {} é impar" .format(number))


viagem= int(input("Digite a distancia da sua viagem em Km: "))
if viagem < 200:
    kmm= viagem * 0.50
    print("Sua viagem custará R${:.2f}" .format(kmm))
else:
    km= viagem * 0.45
    print("Sua viagem custará R${:.2f}" .format(km))


ano= int(input("Coloque um ano: "))
if ano % 4 == 0:
    print("É um ano {} bixesto" .format(ano))
else:
    print(" {} Não é um ano bixesto" .format(ano))

num= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
num3= int(input("Digite um numero: "))
#verificando quem é menor
menor= num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
#verificando quem é maior
maior= num
if num2 > num and num2 > num3:
    maior= num2
if num3 > num and num3 > num2:
    maior= num3
print("O menor valor digitado foi {}" .format(menor))
print("O maior numero digitado foi {}" .format(maior))

salario= float(input("Coloque seu salario: "))
if salario > 1.250:
    a= salario * (10/100)
    b= salario + a
    print("Seu salario com o reajuste é: " ,b, "reais")
else:
    c= salario * (15/100)
    d= salario + c
    print("Seu salario com o reajuste é:" ,d, "reais.")

from random import randint 
computador= randint(0, 5) #faz a maquina escolher um num aleatório
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador= int(input("Em que número eu pensei?"))
if jogador == computador:
    print("PARABÉNS! Voce conseguiu me vencer! ")
else:
    print("GANHEI! Eu pensei no número {} e não no {}" .format(computador, jogador))