def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] < 7 or r['media'] > 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r
    
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)



#Função notas() receber varias notas de alunos
# retornar um dicionario com as seguintes infos 
# quant de notas 
# maior/menor nota 
# media da turma 
# a situação(opcional)
#Tmb add as docstrings da função.
