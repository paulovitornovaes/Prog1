def pegaStr(str):
    tratamentoString = str.split()  # o tratamento é simples, estou aplicando split para separar
    iniciais = ""  # Eu acredito que o "elemento neutro da string seja "" do mesmo jeito que o elemento neutro da soma é zero...
    c = 0  # Vou usar como contador
    for i in range(len(tratamentoString)):
        iniciais += tratamentoString[c][0]  # estou usando o contador para pegar a primeira palavra e o 0 é a primeira letra ex: Paulo Vitor (paulo é o contador no zero e P é o zero, como toda letra inicia no zero, deixo ele fixo
        c += 1  # tenho que sempre adicionar + 1 no contador para pegar a proxima palavra
    return iniciais

#Aqui eu estou fazendo o meu teste
print(pegaStr('Paulo Vitor'))
print(pegaStr('Paulo Vitor Novaes Cardozo'))
