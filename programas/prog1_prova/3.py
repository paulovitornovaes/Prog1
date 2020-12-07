mediaSal = somaTotal = 0
hSelecionados = mSelecionados = maioresAltura = 0
mulheres = homens = 0

for c in range(50):
    nome = str(input("Digite o seu nome: "))
    telefone = int(input("Digite o seu telefone: "))
    sal1 = float(input("Quanto pretende ganhar? R$ "))
    sal2 = float(input("Outro valor salarial: R$ "))
    sal3 = float(input("Outro valor salarial: R$ "))
    mediaSal = (sal1 + sal2 + sal3) / 3
    somaTotal += mediaSal

    sexo = str(input("Sexo (M/F): ").upper())
    if sexo == 'F':
        mulheres += 1
    if sexo == 'M':
        homens += 1

    altura = int(input("Altura cm: "))
    if altura > 170:
        maioresAltura += 1

    print("-" * 45)
    print(f"Nome: , telefone: , sexo: {sexo}, altura: {altura}cm")
    print()

    print(f"Media salarial {mediaSal:.2f}")

    if mediaSal <= 2000:
        print("Candidato selecionado!")
        if sexo == 'M':
            hSelecionados += 1
        if sexo == 'F':
            mSelecionados += 1

    if 2000.01 <= mediaSal <= 2400:
        print("Candidato reservado!")
    if mediaSal > 2400.01:
        print("Candidato descartado!")
    print("-" * 45)

print(f"A media salarial de todos os entrevistados foi {somaTotal / 50:.2f}")
print(f"{mulheres} mulheres foram na entrevista.")
print(f"{maioresAltura} tem mais de 171cm de altura")
