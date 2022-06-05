ex = str(input('Digite a exprssão: '))
pilha= []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida.')
else:
    print('Expressão invalida.')
#O usuario digite uma expressão mat qualquer que use parenteses
#Analisar se os parenteses estão abertos e fechados na ordem certa
