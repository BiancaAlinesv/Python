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
num4= num1 ** 1
print("Seu numero *2 é {}, e *3 é {}, porem sua raiz quadrada fica {}" .format(num2, num3, num4))

#exercicio3
m1=int(input("Digite sua primeira nota: "))
m2=int(input("Digite sua segunda nota: "))
m3= m1 + m2 
m4= m3 / 2
print("A soma das suas notas são {}, então sua média final é {}" .format(m3, m4))