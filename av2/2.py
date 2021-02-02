def fibonacci():
    t1 = 0
    t2 = 1
    t3 = 0  # t3 é o valor proximo
    lista_fibo = []
    for i in range(0, 200):
        lista_fibo.append(t1)
        t3 = t1 + t2  # esse eh sempre o calculo do proximo termo
        t2 = t1
        t1 = t3  # desse jeito o t3 vai ir no append virando t1
    return lista_fibo


# Teste da ordem fibonacci...
print(fibonacci())


def valores_escolhidos():
    valores = []
    for c in range(0, 4):
        numero = int(input("Digite um valor: "))
        valores.append(numero)
    return valores


# Teste dos valores escolhidos...
# print(valores_escolhidos())

# Agora vamos analisar os valores

def analise():
    fibo = fibonacci()
    valores = valores_escolhidos()
    valores_iguais = []
    for c in range(len(fibo)):
        for k in range(len(valores)):
            if fibo[c] == valores[k]:
                valores_iguais.append(valores[k])
    return valores_iguais


def imprime_iguais():
    iguais = analise()
    for i in range(len(iguais)):
        print(f'O valor {iguais[i]} eh compativel com a sequencia!')


imprime_iguais()
