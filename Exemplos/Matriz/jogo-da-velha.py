matriz = [[" "," ", " "],[" "," ", " "],[" "," ", " "]]
gameover = False
total = 0

print("**** INÍCIO ****")

while gameover == False :
    jogada = input("Digite aonde deseja jogar? No formato (linha,coluna) :")
    if jogada != "fim" :
        linha = int(jogada[0])
        coluna = int(jogada[2])

        if total % 2 == 0 :
            if matriz[linha][coluna] == " " :
                matriz[linha][coluna] = "X"
                total += 1
            else :
                print("Essa posição está ocupada, tente outra.")
        else:
            if matriz[linha][coluna] == " " :
                matriz[linha][coluna] = "O"
                total += 1
            else:
                print("Essa posição está ocupada, tente outra.")
    else :
        gameover = True

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if c != len(matriz[l]) - 1:
                print(matriz[l][c], end=" ")
            else:
                print(matriz[l][c])
                if l != len(matriz) - 1:
                    print("---+----+---")
            if c == 0 or c == 1:
                print(" | ", end="")

    print("                                                     FS")
else :
    print("***** GAME OVER *****")