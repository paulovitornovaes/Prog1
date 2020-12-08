contador = inter = gremio = empates = 0
ganhador = ""
while True:
    n = list(map(int, input("").split(" ")))
    contador += 1
    if n[0] > n[1]:
        inter += 1
    elif n[0] < n[1]:
        gremio += 1
    elif inter == gremio:
        empates += 1
    if inter > gremio:
        ganhador = "Inter"
    elif inter < gremio:
        ganhador = "Gremio"
    print("Novo grenal (1-sim 2-nao)")
    novo = int(input(""))
    if novo == 2:
        print(contador, "grenais")
        print("Inter:{}".format(inter))
        print("Gremio:{}".format(gremio))
        print("Empates:{}".format(empates))
        print("{} venceu mais".format(ganhador))
        break
