def notas(*n , sit=False):
    """
    -> Função para analisar notas e a situacao de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando a situacao do aluno
    : return: dicionarios com varias informacoes 
    """
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n)/ len(n)
    if sit:
        if dic['Média'] >= 9:
            dic['Situação'] = 'MUITO BOA'
        elif dic['Média'] >= 7:
            dic['Situação'] = 'BOA'
        elif dic['Média' ] >= 5:
            dic['Situação'] = 'RUIM'
        else:
            dic['Situação'] = 'MUITO RUIM'
    return dic


#Programa principal 
resp= notas(10, sit=True)
print(resp)
# help(notas)