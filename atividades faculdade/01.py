a= float(input("Digite a primeira nota:").replace ("," , "."))
b= float(input("Digite a segunda nota:").replace ("," , "."))
frequencia= int(input("Digite a frequencia do aluno:"))

if (frequencia >= 75):
    soma= a + b
    if(soma >= 6):
        print("Aluno aprovado") 
    elif(soma > 2):
        print("Aluno pode fazer a prova de recuperação")
    else:
        print("Aluno reprovado")
else: 
    print("Aluno reprovado direto")      


    