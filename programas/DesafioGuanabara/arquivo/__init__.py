def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print("Houve algum erro na criacao do arquivo...")
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print("Erro ao ler o arquivo: ")
    else:
        cabecalho