from interface.teste import cabecalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um problema ao crias um arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS!')
        print(a.readlines())
    finally:
        a.close()

def cadastrar(arq, nome= 'desconhecido', idade = 0):
    try: 
        a = open(arq, 'at')
    except:
        print('ERRO NA ABERTURA DO ARQUIVO')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um error na hora de escrver os dados!')
        else:
            print(f'Novo resgistro de {nome} adicionado')
            a.close()
