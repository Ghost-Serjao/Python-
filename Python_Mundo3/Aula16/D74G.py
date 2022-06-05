from random import sample 
num = tuple(sample(range(10), 5))
for i in num:
    print(i, end=' ')
print(f'''
maior valor sorteado: {max(num)}
menor valor sorteado: {min(num)}''')
#GIT HUB

