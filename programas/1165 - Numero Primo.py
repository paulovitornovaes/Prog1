vezes = int(input())
contador = 0
for t in range(vezes):
    n = int(input())
    for c in range(1, n+1):
        if n % c == 0:
            contador += 1
    if contador == 2:
        print("{} eh primo".format(n))
    else:
        print("{} nao eh primo".format(n))
    contador = 0
