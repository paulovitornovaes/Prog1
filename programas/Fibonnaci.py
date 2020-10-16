n = int(input("Digite um numero para ver o fibonnaci: "))
if n < 46:
    t1 = 0
    t2 = 1
    print('{}  {}'.format(t1, t2), end='')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print('  {}'.format(t3), end='')
        cont += 1
