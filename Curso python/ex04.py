from random import choice
n1= str(input("Primeiro aluno:"))
n2= str(input("Segundo aluno:"))
n3= str(input("Terceiro aluno:"))
n4= str(input("Quarto aluno:"))
lista= [n1, n2, n3, n4]
escolhido= choice(lista)
print("O aluno escolhido foi {}" .format(escolhido))


from random import shuffle
a1= str(input("Primeiro aluno: ")) 
a2= str(input("Segundo aluno: "))
a3= str(input("Terceiro aluno: "))
a4= str(input("Quarto aluno: "))
lista= [ a1, a2, a3, a4]
shuffle(lista)
print("A ordem de apresentação é")
print(lista)
