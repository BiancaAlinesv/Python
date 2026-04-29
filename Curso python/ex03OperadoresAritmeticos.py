nome=input("Qual é seu nome? ")
print("Olá {:=^20}".format(nome))   #{:=^20} (20 espaço que vai ter na variavel) (=- vai aparecer antes e depois no texto digitado)  (^ centraliza o texto)

n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2 
e= n1 ** n2
print("A soma é {}, o produto é {} e a divisao é {:.3f}" .format( s, m, d), end= ", ")  # ({:.3f}- 3/numero decimal que quero; f/float)  (end= "", não tem quebra de linha entre o print de baixo) (\n- nova linha sem precisar do print)
print("Divisão inteira {} e potencia {}" .format(di, e))

#exercicio1
n1=int(input("Digite um número: "))
n2= n1 - 1
n3= n1 + 1
print("Seu numero -1 é igual a {}, e com +1 fica {}" .format(n2, n3))

#exercicio2
num1=int(input("Digita um numero: "))
num2= num1 * 2
num3= num1 * 3
num4= num1 ** (1/2)
print("Seu numero *2 é {}, e *3 é {}, porem sua raiz quadrada fica {}" .format(num2, num3, num4))

#exercicio3
m1=int(input("Digite sua primeira nota: "))
m2=int(input("Digite sua segunda nota: "))
m3= m1 + m2 
m4= m3 / 2
print("A soma das suas notas são {}, então sua média final é {}" .format(m3, m4))


meters=float(input("Digite sua altura: "))
calc= meters * 100
print("Voce tem {} centimetros" .format(calc))

tab=int(input("Digite um número: "))
tab1= tab * 1 
tab2= tab * 2
tab3= tab * 3
tab4= tab * 4
tab5= tab * 5
tab6= tab * 6
tab7= tab * 7
tab8= tab * 8
tab9= tab * 9
tab10= tab * 10
print("Seu numero é {}, e a tabuada dele é: \n {} * 1 = {} \n {} * 2 = {} \n {} * 3 = {} \n {} * 4 = {} \n {} * 5 = {} \n {} * 6 = {} \n {} * 7 = {} \n {} * 8 = {} \n {} * 9 = {} \n {} * 10 = {}" .format(tab, tab, tab1, tab, tab2, tab, tab3, tab, tab4, tab, tab5, tab, tab6, tab, tab7, tab, tab8, tab, tab9, tab, tab10 ))

dollar=float(input("Tem quanta grana aí?"))
dollar1=dollar / 4.99
print("Voce tem {:.2f} dolares" .format(dollar1))

width=float(input("Digite a largura de sua parede:"))
height=float(input("Agora a altura:"))
m4= width * height
total= m4 / 2
print("Sua parede tem {} m². \n Voce precisara de {} litros para pinta-lá." .format(m4, total))

price=float(input("Qual o valor do produto?")) 
discount=float( price * (5 / 100))
end= price - discount
print("Seu produto custa {}, porém com o desconto de ficou {}" .format(price, end)) 

payment=float(input("Qual o valor do se salário?"))
bonus=float( payment * ( 15 / 100))
calculate= payment + bonus
print("Parabens!!!! Seu salário com o bonus fica {:.3f}" .format(calculate))