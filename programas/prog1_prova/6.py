fatorial = fatorial2 = 1
fatorialTotal = 0
while True:
    fatorial = fatorial2 = 1
    m = int(input("Digite o primeiro valor: "))
    n = int(input("Digite o segundo valor: "))
    for c in range(m):
        fatorial *= (c + 1)
    print(f"O primeiro fatorial vale {fatorial}")
    for i in range(n):
        fatorial2 *= (i + 1)
    print(f"O segundo fatorial vale {fatorial2}")
    print(f"A soma dos dois fatoriais vale {fatorial + fatorial2}")
    fatorialTotal += fatorial + fatorial2
    if fatorialTotal != (fatorial + fatorial2):
        print(f"A soma total de todos fatoriais vale {fatorialTotal}")
