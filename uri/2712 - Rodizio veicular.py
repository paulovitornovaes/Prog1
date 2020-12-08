def checkNum(var):
    var = var[4:8]
    try:
        int(var)
    except ValueError:
        return False
    return True


def checkSpecial(var):
    if placa[3] == "caracter '-'":
        return True
    else:
        return False


def checkAlpha(var):
    var = var[0:2]
    if var.isalpha():
        return True
    else:
        return False


for i in range(int(input())):
    placa = input()
    if not checkAlpha(placa) and not checkNum(placa) and not checkSpecial(placa) and not placa.isupper() and len(placa) !=7:
        print("FAILURE")
    else:
        if placa[7] == '1' or placa[7] == '2':
            print('MONDAY')

        elif placa[7] == '3' or placa[7] == '4':
            print('TUESDAY')

        elif placa[7] == '5' or placa[7] == '6':
            print('WEDNESDAY')

        elif placa[7] == '7' or placa[7] == '8':
            print('THURSDAY')

        elif placa[7] == '9' or placa[7] == '0':
            print('FRIDAY')

