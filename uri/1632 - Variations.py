t = int(input())
calc = 1
for c in range(t):
    password = str(input().strip())
    for i in range(len(password)):
        if 'A' in password[i] or 'E' in password[i] or 'I' in password[i] or 'O' in password[i] or 'S' in password[i] \
                or 'a' in password[i] or 'e' in password[i] or 'i' in password[i] or 'o' in password[i] or 's' in \
                password[i]:
            calc *= 3
        else:
            calc *= 2

    print(calc)
    calc = 1
