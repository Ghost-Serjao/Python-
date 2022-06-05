somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
  print(f'--------{p}ª PESSOA --------')
  nome = str(input('Nome:')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip()
  somaidade += idade
  if p == 1 and sexo in 'Mm':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = nome 
  if sexo in 'Ff' and idade > 20:
    totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho é {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')







#LER: NOME, IDADE, SEXO de 4 pessoas
#A media de idade
#Nome do homem mais velho
#Quantas mulheres tem menos de 21