#Adicionar dicionarios a listas
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#Vai mostrar uma lista com 2 elementos (estado1) e (estado2)
print(brasil)
#Mostrar o estado1
print(brasil[0])
#Mostrar estado2 
print(brasil[1])
#Mostrar 'Rio de Janeiro'
print(brasil[0]['uf'])
#Mostrar 'SP'
print(brasil[1]['sigla'])

#Repetição com for

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #.copy() é o [:] do dicionario
    brasil.append(estado.copy()) 
print(brasil)
#Mostra cada estado
for e in brasil:
    print(e)
for e in brasil:
    #Motra os itens relacionados dentro de e(brasil) Ex:'Uf tem valor Rio de Janeiro', 'sigla tem valor RJ'
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}' )
#so para valores
for e in brasil:
    for v in e.value():
        print(v)