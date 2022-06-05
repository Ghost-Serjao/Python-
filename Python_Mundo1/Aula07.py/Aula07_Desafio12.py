print('Preço do produto com 5% de desconto')
preço = float(input('Qual o preço do produto R$:'))
desconto = (5 * preço) / 100
novo = preço - desconto
print(f'O preço do produto com desconto de 5% sera R$:{novo:.2f}')