def inverter(numero) :
    if numero == 0 :
        return 0
    else :
        print(numero%10, end = " ")
        numero = numero // 10
        return inverter(numero)

x = 123
print(inverter(x))
