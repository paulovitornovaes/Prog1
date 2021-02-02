n = int(input())
soma = 0

for i in range(n):
    leds = str(input())
    for c in leds:
        if int(c) == 1:
            soma += 2
        elif int(c) == 2 or int(c) == 3 or int(c) == 5:
            soma += 5
        elif int(c) == 4:
            soma += 4
        elif int(c) == 6 or int(c) == 9 or int(c) == 0:
            soma += 6
        elif int(c) == 7:
            soma += 3
        elif int(c) == 8:
            soma += 7
    print(soma, 'leds')
    soma = 0
