from interface import teste
from arquivo import arq

arqv = 'Pessoas adicionadas.txt'
if not arq.arquivoExiste(arqv):
    arq.criarArquivo(arqv)

while True:
    resposta = teste.menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        arq.lerArquivo(arqv)
    elif resposta == 2:
        teste.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = teste.leiaint('Idade: ')
        arq.cadastrar(arqv, nome, idade)
    elif resposta == 3:
        teste.cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Opção inválida\033[m')
