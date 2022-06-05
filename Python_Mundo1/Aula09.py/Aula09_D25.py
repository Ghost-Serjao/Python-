#ler o nome e ver se tem 'Silva' no nome
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))