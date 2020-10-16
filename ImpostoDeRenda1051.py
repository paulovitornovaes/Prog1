n = float(input())

if n <= 2000.00:
    print("Isento")
else:
    if 2000.01 <= n <= 3000.00:
        n -= 2000
        taxa8 = n * 0.08
        print("R$ {:.2f}".format(taxa8))
    elif 3000.01 <= n <= 4500.00:
        n -= 2000
        taxa8 = 1000 * 0.08
        n -= 1000
        taxa18 = n * 0.18
        print("R$ {:.2f}".format(taxa8+taxa18))
    elif n > 4500.00:
        n -= 2000
        taxa8 = 1000 * 0.08
        n -= 1000
        taxa18 = 1500 * 0.18
        n -= 1500
        taxa28 = n * 0.28
        print("R$ {:.2f}".format(taxa8+taxa18+taxa28))
