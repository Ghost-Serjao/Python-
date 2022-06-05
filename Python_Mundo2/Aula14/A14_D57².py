sexo = str(input('Digite seu sexo [M/F]'))[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor informe seu sexo: ')).striper().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
