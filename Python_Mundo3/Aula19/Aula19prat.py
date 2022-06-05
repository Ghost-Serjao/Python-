
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
#Trocar o nome de um elmento
pessoas['nome'] = 'lenadro'
#Add elemento
pessoas['peso'] = 98.5
#vai apagar o elemento sexo e so mostrar os outros
del pessoas['sexo']
#Vai mostrar tudo
print(pessoas) 
#vai mostrar so um elemento
print(pessoas['nome'])
#Usar aspas duplas dentro print formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#Mostrar as chaves (nome, sexo, idade)
print(pessoas.keys())
#Mostrar os valores(gustavo, m, 22)
print(pessoas.values())
#Mostrar tudo 
print(pessoas.items())
#Acessar por laço
#Mostra so as chaves
for k in pessoas.keys():
    print(k)
#Mostra so os valores
for k in pessoas.values():
    print(k)
#Mostrar tudo precisa de chave(K) e valor(V)
for k, v in pessoas.items():
    print(f'O {k} = {v}')
