nome = str(input('Digite seu nome completo: ')).strip()
print('ANALISANDO SEU NOME...')
print('Seu nome em maiusculas é:{}'.format(nome.upper()))
print('Seu nome em minusculas é:{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('seu 1° nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


#ler o nome completo de uma pessoa e mostre
#com todas as letras maiusculas
#minusculas
#quantas letras sem considerar espaços
#quantas letras tem o 1° nome
