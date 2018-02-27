x = [[5,0,0],[0,5,0],[0,0,5]]

for linha in range(0, len(x)) :
    for coluna in range(0, len(x[linha])) :
        if linha == coluna :
            print(x[linha][coluna])
