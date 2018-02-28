matriz = [["0","0","0"],["x","x","x"],["0","0","0"]]

print("\n")

for linha in range(len(matriz)) :
    for coluna in range(len(matriz[linha])) :
        if coluna != len(matriz[linha]) -1 :
            print(matriz[linha][coluna], end = "")
        else :
            print(matriz[linha][coluna])
            if linha != len(matriz) - 1 :
                print("-+-+-")
        if coluna == 0 or coluna == 1 :
            print("|", end = "")

print("\n")
