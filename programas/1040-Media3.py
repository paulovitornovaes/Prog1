n = list(map(float, input("").split()))

media = ((n[0] * 2) + (n[1] * 3) + (n[2] * 4) + (n[3])) / 10
print("Media: {:.1f}".format(media))

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif 5 <= media <= 6.9:
    print("Aluno em exame.")
    new = float(input(""))
    print("Nota do exame: {:.1f}".format(new))
    nova_media = (media + new) / 2
    if nova_media >= 5:
        print("Aluno aprovado.")
    elif nova_media < 5:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(nova_media))


