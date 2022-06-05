preço = float(input('Valor do produto: '))
forma = str(input('Forma de pagamento: \n[1] Dinheiro \n[2] Avista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão \nDigite aqui:  '))
if forma == ('1'):
    desconto = preço - (preço * 10) / 100
    print(f'Com desconto de 10%\nO valor passara a ser de R${desconto}')
elif forma == ('2'):
    desconto = preço - (preço * 5) / 100
    print(f'Com desconto de 5%\nO valor passara a ser de R${desconto}')
elif forma == ('3'):                   
    print(f'Em 2x não tem desconto, preço:R${preço}')
elif forma == ('4'):
    jurus = preço + (preço * 20) / 100
    print(f'Em 3x a acressimo de 20% de jurus, o valor passa a ser R${jurus}')








#calcular o valor a ser pago considerando seu preço normal e a forma de pagamento 
#avista (dinheiro/cheque): 10% de desconto 
#avista cartão: 5% desconto
#ate 2x no cartão preço normal
#3x ou mais no cartão 20% de jurus 