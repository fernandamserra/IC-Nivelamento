def soma_lista(lista) :
    aux = 0
    for i in range(len(lista)) :
        aux += lista[i]
    return aux

x = [1,1,1]
print(soma_lista(x))