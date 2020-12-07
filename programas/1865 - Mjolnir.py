c = int(input())
for i in range(c):
    nome, newton = (input().split())
    if 'thor' in nome.lower():
        print('Y')
    else:
        print('N')


