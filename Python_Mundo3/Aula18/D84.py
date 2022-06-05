temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os dados forma {princ}')
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'''
O maior peso foi de {mai}Kg.
o menor peso foi de {men}Kg.''')





#Ler nome/peso de varias pessoas e guadar em um lista
#A numero de pessoas 
#B pessoas mais pesadas 
# pessoas mais leves