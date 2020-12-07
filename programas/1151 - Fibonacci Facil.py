n = int(input())
x1 = x3 = 0
x2 = 1
print("{} {} ".format(x1, x2), end='')
for c in range(0, n-2):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    if (c + 3) == n:
        print(f"{x3}")
        break
    print('{} '.format(x3), end='')
