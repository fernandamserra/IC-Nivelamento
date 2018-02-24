x = 0
aux = 0
total = 0
numeros = []
while x != -1 :
    x = int(input("Digite um número :"))
    numeros.append(x)
    aux = aux + 1
else:
    for i in range(aux) :
        total = total + numeros[i]

    print("A soma dos números é :", total + 1)