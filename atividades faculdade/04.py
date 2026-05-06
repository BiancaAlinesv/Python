listaNomes= []  # .append adciona um novo elemento a lista
listaNomes.append("João")
listaNomes.append("Maria")
listaNomes.append("Anna")
listaNomes.append("Clara")

minhaLista= ["João", "Maria", "Anna", "Silva"]  
for elementos in minhaLista:
    print(elementos)


minhaLista= [1, "Silva", "4.5"]
minhaLista[0]=2
minhaLista[1]= "João da Silva"
for elementos in minhaLista:
    print(elementos)

minhaLista= ["João", "Maria", "Pedro", "Aló Virginia"] 
minhaLista.remove("Maria") # Removo um item espcifico da lista
minhaLista.pop() #Remove o ultmo item da lista
print(minhaLista)


tupla= (1, 2, 3, 4, 5, 6) # tupla não permite alteraçoes ou exclusão
del tupla # exclui
 # Identificando tupla

meuDicionario= {"Nome": "João da Silva", "idade": 25}  #dicionario é com se fosse uma lista de contatos de celular chave: nome/ valor: João da Silva


nome= ("anna", "fernanda", "maria")
nome.append("lucas")
print(nome)