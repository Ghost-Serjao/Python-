print('Preço do produto com 70% de desconto')
preço = float(input('Qual o preço do produto R$:'))
novo = preço - (preço * 70 / 100)
print(f'O preço do produto com desconto de 5% sera R$:{novo:.2f}')
