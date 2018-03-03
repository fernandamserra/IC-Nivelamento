def soma_matriz(matriz):
    aux = 0
    for linha in range(len(matriz)) :
        for coluna in range(len(matriz[linha])) :
            aux += matriz[linha][coluna]
    return aux

x = [[1,1,1],[1,1,1],[1,1,1]]
print(soma_matriz(x))