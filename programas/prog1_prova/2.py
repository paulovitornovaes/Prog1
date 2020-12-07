positivos = nulos = negativos = 0
somaPositivo = somaNegativo = 0
contadorPositivo = contadorNegativo = 0
for c in range(60):
    valor = int(input("Digite um valor para ser analisado: "))
    if valor > 0:
        positivos += 1
        contadorPositivo += 1
        somaPositivo += valor
    if valor == 0:
        nulos += 1
    if valor < 0:
        negativos += 1
        contadorNegativo += 1
        somaNegativo -= valor

print(f"Foram computados {positivos} positivo(s), {nulos} nulo(s) e {negativos} negativo(s)!")
if contadorPositivo > 0:
    print(f"A media dos valores positivos foi de {somaPositivo / contadorPositivo}")
else:
    print("Nao foi escolhido nenhum valor positivo, por isso nao ha nenhuma media dos positivos")

if contadorNegativo > 0:
    mediaNegativo = -somaNegativo / contadorNegativo
    print(f"A media dos valores negativos foi de {mediaNegativo}")
else:
    print("Nao foi escolhido nenhum valor negativo, por isso nao ha nenhuma media dos negativos")
