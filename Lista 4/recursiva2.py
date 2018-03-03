def contagem(num) :
    if num == 0 :
        print("0")
    else :
        aux = 0
        for i in range(num + 1) :
            aux += i

        print(aux)


x = int(input("DIgite um número inteiro :"))
print(contagem(x))
