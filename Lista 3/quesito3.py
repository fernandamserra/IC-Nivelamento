x = ""
lista = []

while x != "fim" :
    x = input("Digite um item pra adicionar na lista :")
    if x != "fim" :
        lista.append(x)
else :
    print("\n")
    print("\n")
    
    print("LISTA DE COMPRAS :")
    for i in range(len(lista)):
        print(lista[i])