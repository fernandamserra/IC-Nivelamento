def potencia (num,exp) :
    if num == 1 :
        print("1")
    else :
        y = 0
        for i in range(exp + 1) :
            y = pow(num,potencia(num, exp - 1))

        print(y)


n = 2
e = 3
print(potencia(n,e))
