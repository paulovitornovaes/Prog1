n = int(input("leia um valor inteiro: "))
print(f"O valor escolhido foi R$:{n}")
ced100 = n // 100
n %= 100
print(f"{ced100} notas de R$ 100")
ced50 = n // 50
n %= 50
print(f"{ced50} notas de R$ 50")
ced20 = n // 20
n %= 20
print(f"{ced20} notas de R$ 20")
ced10 = n // 10
n %= 10
print(f"{ced10} notas de R$ 10")
ced5 = n // 5
n %= 5
print(f"{ced5} notas de R$ 5")
ced2 = n // 2
n %= 2
print(f"{ced2} notas de R$ 2")
print(f"{n} notas de R$ 1")