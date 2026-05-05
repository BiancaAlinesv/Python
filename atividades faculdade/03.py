for i in range(10, -1, -1):
  print("Valor de i: " + str(i))


soma= 0
for i in range(10):
  soma= soma+3
  print(soma)


tab= 0
for i in range(10):
  tab= tab + 8
  print(tab)
    

for i in range(0, 15, 2):
    print(i)

qtdMultiplos= 0
for i in range(1, 10):
    if(i%3==0):
       qtdMultiplos+=1
       print(i)


contador= 0
while (contador < 10):
   contador +=1
   print(contador)


nome= ""
while True:
   texto= input("Digite um nome ou '0' para encerrar o programa ")

   if(texto == "0"):
      print("Programa finalizado")
      break
   else:
      nome = nome + texto + "\n"
      print(nome)

texto="Bianca"
for i in texto:
   print(i)

sexo = ""
idade= 0
qntMulheres= 0
valorIdade= 0
for i in range(0,3):
   sexo= input("Digite o sexo (M ou H)")
   idade= int(input("Digite a idade: "))

   if(sexo=="M" or sexo=="m"):
      qntMulheres+=1
   valorIdade+= idade
mediaIdade= valorIdade/qntMulheres 
print("A quantidade de mulheres é", qntMulheres)
print("A média de idade das mulheres é", mediaIdade)


sexo = ""
idade= 0
qntMulheres= 0
qntHomens= 0
for i in range(0,5):
   sexo= input("Digite o sexo (M ou H)")
   idade= int(input("Digite a idade: "))

   if(sexo=="M" or sexo=="m"):
      qntMulheres+=1
   elif(sexo=="H" or sexo=="h"):
      qntHomens+=1
print("A quantidade de mulheres é", qntMulheres)
print("A quantidade de homens é", qntHomens)

valor= 0
for i in range(3):
   valor= float(input("Digite um valor"))
print(valor)


contador= 0
notas= 0
while contador < 6:
   notas= float(input("Digite a nota do aluno"))
media= notas/contador
print("A média de notas é", media)
