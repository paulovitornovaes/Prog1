def lerArquivo(texto, lista):  # vou precisar abrir o arquivo
    # (como minha variavel para abrir o arquivo se chama arquivo,
    # decidi chamar aqui de texto ja que tenho que selecionar um arquivo txt)
    arquivo = open(texto, 'r')
    leitura = arquivo.readlines()
    for linha in leitura:
        lista.append(int(linha))
    arquivo.close()


def colocaPares(lista, pares):
    for i in lista:
        if i % 2 == 0:
            pares.append(i)


def colocaImpares(lista, impares):
    for i in lista:
        if i % 2 != 0:
            impares.append(i)

#estou criando um arquivo para pares e um arquivo para impares
def escrita(pares, impares):
    arquivoPares = open('pares.txt', 'w')
    arquivoImpares = open('impares.txt', 'w')
    for i in pares:
        arquivoPares.write(str(i) + "\n") #preciso escrever uma string(i) = valor par e depois pular linha
    for i in impares:
        arquivoImpares.write(str(i) + "\n")

# essa parte eh para fazer o teste
lista = []
impares = []
pares = []

lerArquivo("int.txt", lista)
colocaPares(lista, pares)
colocaImpares(lista, impares)
escrita(pares, impares)
