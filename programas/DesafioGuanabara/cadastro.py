from DesafioGuanabara.interface import *

while True:
    resposta = menu(['Criar arquivo', 'Cadastrar pessoas', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        print('Opcao 1')
    elif resposta == 2:
        print('Opcao 2')
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print("ERRO! Digite uma opcao valida!")
