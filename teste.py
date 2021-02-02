def lerArquivo(arq):
    numeros=[]
    for linha in arq:
        numeros.append(int(linha.strip("\n")))
    return numeros

def escreveArquivo(arq, num):
    arq.write(f"{num}\n")
    return None

nomeArq = input()
dados = open(nomeArq,"r", encoding="utf-8")
par = open("par", "a", encoding="utf-8")
impar = open("impar","a",encoding="utf-8")

lista = lerArquivo(dados)
for numero in lista:
    if numero%2==0:
        escreveArquivo(par,numero)
    else:
        escreveArquivo(impar, numero)

dados.close()
par.close()
impar.close()