x = int(input("Digite o valor de x: "))
valorTotal = 0
fatorial = 1
frente = True
for c in range(10):
    expoente = c + 2
    valor = x ** expoente
    if expoente % 2 == 0:
        valor = -valor
    valorFat = 1
    for n in range(1, fatorial + 1):
        valorFat *= n
    valorFracao = valor / valorFat
    valorTotal += valorFracao
    if fatorial == 1:
        frente = True
    if fatorial == 4:
        frente = False
    if frente:
        fatorial = fatorial + 1
    else:
        fatorial = fatorial - 1
print(f"A soma desses valores vale {valorTotal}")
