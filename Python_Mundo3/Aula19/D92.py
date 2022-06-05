from datetime import date
dados = {}
print('==PREENCHA SEUS DADOS ABAIXO==')
dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - dados['nasc'] 
dados['carteira'] = int(input('Carteira de trabalho(0 = não tem): '))
if dados['carteira'] == 0:
    print('Ainda não possui Carteira de trabalho!')   
else:
    dados['contr'] = int(input('Ano de contratação: '))
    aposento = 35 + dados['contr']
    idadep = idade + aposento - 2000
    dados['Sala'] = float(input('Salário:R$ '))
    print(f'{dados["nome"]} se aposentara em {aposento} com {idadep} anos.')
      
#ler nome, ano de nasc, carteira de trabalho e cadastre( com idade )em um dicionario
#se o carteira fo != 0 fo dicionario recebera o ano de contratação e o salario
#com quantos anos a pessoa vai se aposentar (aposenta depois de 35 de contribuição) 
