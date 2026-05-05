#Manipulando texto
frase= "Curso em Vídeo Python"
print(frase[1:13:2])

frase1="Curso em video"
print(frase1.upper())

#exercicio1
name= input("Digite seu nome completo: ")
print(name.upper())
print(name.lower())
print (len(name))
print(name.split()[0])
primeiro= name.split()[0]
print(len(primeiro))  

#exercicio2
number= input("Digite um número até 9999: ")
print(len(number))
print(number[2])
print(number[1])
print(number[0])

#exercicio3
city= input("Digite sua cidade: ")
print (city in "Santo, santo")