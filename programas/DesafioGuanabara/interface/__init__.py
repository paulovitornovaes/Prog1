def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())
    return None


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    return None
