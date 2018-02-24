lista = ["vontade de viver","memes","drogas","adesivo de nicotina"]
x = ""

print("****** LISTA DE COMPRAS ******")
for i in range(len(lista)):
    print(lista[i])

while x != "fim" :
    x = input("Digite o nome do item que deseja excluir:")
    if x != "fim" :
        lista.remove(x)
else :
    print("\n")
    print("\n")

    print("*****LISTA DE COMPRAS ******")
    for i in range(len(lista)):
        print(lista[i])