#Menor que 18,5 - Abaixo do peso
#Entre 18,5 e 25,0 - Peso normal
#Entre 25,0 e 30,0 - Pré-obesidade
#Entre 30,0 e 35,0 - Obesidade Grau 1
#Entre 35,0 e 40,0 - Obesidade Grau 2
#Acima de 40 - Obesidade Grau 3
# >= 20 anos
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))
imc = peso / (altura * altura)
if idade >= 20:
    print("Seu IMC é: ", imc)
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 25:
        print("Peso normal")
    elif imc >= 25 and imc <= 30:
        print("Pré-Obesidade")
    elif imc >= 30 and imc <= 35:
        print("Obesidade Grau 1")
    elif imc >= 35 and imc <= 40:
        print("Obesidade Grau 2")
    elif imc >= 40:
        print("Obesidade Grau 3")
else:
    sexo = input("Digite seu sexo (M/F): ")
    if sexo == "M":
        if idade == 10:
            if imc < 14.42:
                print("Baixo Peso")
            elif imc <= 19.60:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 11:
            if imc < 14.83:
                print("Baixo Peso")
            elif imc <= 20.35:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 12:
            if imc < 15.24:
                print("Baixo Peso")
            elif imc <= 21.12:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 13:
            if imc < 15.72:
                print("Baixo Peso")
            elif imc <= 21.92:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 14:
            if imc < 16.18:
                print("Baixo Peso")
            elif imc <= 22.77:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 15:
            if imc < 16.59:
                print("Baixo Peso")
            elif imc <= 23.63:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 16:
            if imc < 17.31:
                print("Baixo Peso")
            elif imc <= 25.28:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 17:
            if imc < 17.31:
                print("Baixo Peso")
            elif imc <= 25.28:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 18:
            if imc < 17.54:
                print("Baixo Peso")
            elif imc <= 25.95:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 19:
            if imc < 17.80:
                print("Baixo Peso")
            elif imc <= 26.96:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
    else:
        if idade == 10:
            if imc < 14.23:
                print("Baixo Peso")
            elif imc <= 20.19:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 11:
            if imc < 14.60:
                print("Baixo Peso")
            elif imc <= 21.18:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 12:
            if imc < 14.98:
                print("Baixo Peso")
            elif imc <= 22.17:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 13:
            if imc < 15.36:
                print("Baixo Peso")
            elif imc <= 23.08:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 14:
            if imc < 15.67:
                print("Baixo Peso")
            elif imc <= 23.88:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 15:
            if imc < 16.01:
                print("Baixo Peso")
            elif imc <= 24.29:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 16:
            if imc < 16.37:
                print("Baixo Peso")
            elif imc <= 24.74:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 17:
            if imc < 16.59:
                print("Baixo Peso")
            elif imc <= 25.23:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        elif idade == 18:
            if imc < 16.71:
                print("Baixo Peso")
            elif imc <= 25.56:
                print("Peso Adequado")
            else:
                print("Sobrepeso")
        else:
            if imc < 16.87:
                print("Baixo Peso")
            elif imc <= 25.85:
                print("Peso Adequado")
            else:
                print("Sobrepeso")