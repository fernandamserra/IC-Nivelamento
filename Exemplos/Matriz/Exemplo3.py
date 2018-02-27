x = [[0,0,5],[0,5,0],[5,0,0]]

for linha in range(0, len(x)) :
    for coluna in range(0 , len(x[linha])) :
        if linha + coluna == len(x[linha]) - 1 :
            print(x[linha][coluna])
