L = ['banana','leite','maca','ovo','pao','uva','biscoito','suco']
pos = -1

x = input("Digite um item que deseja buscar na lista :")

for i in range(len(L)) :
    if x == L[i]:
        pos = i
        print("Posição do item '"+ x +"' é : ", pos)

if pos == -1 :
    print("Non foundei):")