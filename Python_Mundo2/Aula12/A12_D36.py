print('----------EMPRESTIMO CASA----------')
print('======================================')
print('PREENCHA O FORMULARIO ABAIXO')
print('======================================')
valor = float(input('Valor da casa R$'))
salario = float(input('Seu salario R$'))
anos_pagar = int(input('Em quantos anos deseja pagar:'))
parcela = valor / (anos_pagar * 12)
if salario < (parcela * 30) / 100:
    print(f'Emprestimo negado, pois o valor da parcela seria de R${parcela:.2f} e ultrapassa 30% do seu salario.\nDesculpe')
elif salario > (parcela * 30) / 100: 
    print(f'Emprestimo aprovado, o valor da parcela sera de R${parcela:.2f} ! Parabens!')
print('---------------VOLTE SEMPRE QUE PRECISAR---------------')

#Emprestimo para comprar casa
#perguntar: Valor da casa, salario do comprador, quantos anos ele vai pagar
#calcular valor das parcelas sabendo que ela não pode passar de 30% do salario 
#senão emprestimo negado
#Valor da casa / quantidade de Anos (meses)