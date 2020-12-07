n = 0


def menu():
    print("-" * 30)
    print("1 - Cadastrar outra pessoa: ")
    print("2 - Ver todos os cadastros: ")
    print("3 - sair")
    print("-" * 30)


while n != 3:
    file = open('xd.txt', 'w+')
    name = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    file.write(name)
    file.write(str(idade))
    menu()
    print()
    n = int(input("Faca sua escolha: "))
    if n == 2:
        print(file.read())
