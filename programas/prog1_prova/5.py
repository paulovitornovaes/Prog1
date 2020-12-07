q = int(input("Digite a quantidade de casos: "))

for c in range(q):
    m = int(input("Digite o primeiro valor: "))
    n = int(input("Digite o segundo valor: "))
    if m % 2 != 0:
        m += 1
    total = m

    for d in range(n-1):
        calculo = m + 2
        m += 2
        total += m

    print(total)
