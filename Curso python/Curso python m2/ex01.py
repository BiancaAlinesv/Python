#exercicio 1
imovel= float(input("Digite o valor do imovel: ").replace(",", "."))
salario= float(input("Digite o valor do seu salário: ").replace(",", "."))
anos= int(input("Em quantos anos pretende pagar?: "))

prestacoes= imovel / (anos*12)

if prestacoes <= salario * 0.30:
    print("Enprestimo aprovado! \nValor das prestações será R${:.2f}" .format(prestacoes))
elif prestacoes >= salario *0.30:
    print("Emprestimo negado! \nO valor da prestacoes seria R${:.2f} ultrapassa as condicoes exigidas" .format(prestacoes))

#exercicio 2
number= int(input("Digite um número inteiro: "))
convert= input("Escolha uma base para conversão: \n1-Binário \n2-Octal \n3_Hexadecimal: \n")
if convert == "1":
    print("{} convertido para binário é {}" .format(number, bin(number)))
elif convert == "2":
    print("{} convertido para octal é {} " .format (number, oct(number)))
elif convert == "3":
    print("{} convertido para hexadecimal é {}" .format(number, hex(number)))
else:
    print("Opção invalida! Escolha entre 1, 2 ou 3!")
    
    

#exercicio 3
num= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
if num > num2:
    print("O numero{} é maior que o numero {}" . format(num, num2))
elif num2 > num:
    print("O numero {} é maior que {}" .format(num2, num))
elif num == num2:
    print("Não existe valor maior, os dois são iguais")
    
    
#exercicio 4
import datetime 

year= int(input("qual o ano de seu nascimento?: "))
gender= input("Qual seu genero?: \nMaculino-M \n Feminino-F \n")
year= datetime.datetime.now().year-year

if gender.upper() == "M":
    if year == 18:
        print("Voce precisa se alistar esse ano!")
    elif year < 18:
        print("Ainda falta {} anos para se alistar" .format(18 -year))
    elif year > 18:
        print("Voce já deveria ter se alistado há {} anos".format(year-18))
else:
    print("Voce é do sexo feminino, não precisa se alistar!")  
    
    
#exercicio 5
notice= float(input("Digite a primeira nota do aluno: "))
notice2= float(input("Digite a segunda nota do aluno: "))
average= (notice + notice2) / 2
if average < 5:
    print("O aluno foi reprovado Média: {:.1f}" .format(average))
elif average <6.9:
    print("O aluno ficará em recuperação Média: {:.1f}" .format(average))
elif average > 7:
    print("Aluno aprovado! Média: {:.1f}" .format(average))
    
    
#exercicio 6
import datetime
year= int(input("Digite o ano de nescimento do atleta: "))
date= datetime.datetime.now().year
age= date - year
if age <= 9:
    print("Atleta mirim")
elif age <= 14:
    print("Atleta infantil")
elif age <= 19:
    print("Atleta junior")
elif age <= 20:
    print("Atleta senior")
else:
    print("Atleta master")


#exercicio 8
calc= float(input("Digite sua altura: "))
weight= float(input("Digite seu peso: "))
imc= weight / (calc * calc)
if imc < 18.5:
    print("Voce está abaixo do peso")
elif imc < 25:
    print("Voce está com o peso ideal")
elif imc < 30:
    print("Voce está com sobrepeso")
elif imc < 40:
    print("Voce está obeso")
elif imc > 40:
    print("Voce está com obesidade mórbida") 
    
    
#exercicio 9
price= float(input("Digite o valor do produto: "))
payment= int(input("Qual a forma de pagamento?:\n 1-À vista: Dinheiro/cheque. \n 2-À vista no cartão \n 3-Parcelado até 2vx no cartão \n 4-Parcelado 3vx ou mais no cartao \n"))
if payment == 1:
    discount= price * 0.10
    final_price= price - discount
    print("O valor final do produto é R${:.2f}" . format(final_price))
elif payment == 2:
    discount= price * 0.05
    final_price= price - discount
    print("O valor final do produto é R${:.2f}" .format(final_price))
elif payment == 3:
    print("O valor final do produto é R${:.2f}" .format(price))
elif payment == 4:
    installment= price * 0.20
    final_price= price + installment
    print("O valor final do seu produto é R${:.2f}" .format(final_price))





