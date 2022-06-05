dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
#Adicionar elento ao dicionario
dados['sexo'] = 'M'
#Remover elemnetos
del dados['idade']
#O importante é fechar as chaves {}
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }
#Mostra todos os valores(Star Wars', 1977, 'George Lucas')
print(filme.values()) 
#Mostra todas as chaves ('titulo', 'ano', 'idade')
print(filme.keys())
#Mostrar todos os valores
print(filme.items())
#Utilizar nos laços
#Criar uma variavel para keys(k) E values (v)
for k, v in filme.items():
     #No primeiro laço do for vai mostrar 'O titulo é Star Wars'
    print(f'o {k} é {v}')
    #Quando o For voltar vai mostra 'O ano é 1977'
    #Depois vai mostrar 'O diretor é George Lucas'
    #Por fim termina o laço

#Pode juntar lista tuplas e dicionarios 

locadora = [[{'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}],
            [{'titulo':'Avengers', 'ano':2012, 'diretor':'Joss Whedon'}],
            [{'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}]
           ]

