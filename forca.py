print("******** JOGO DA FORCA ********")
palavra = input("Digite a palavra secreta : ")

for i in range(10) :
    print("\n")

print("********* INICIO **********")

suicida = ["||=====:====","||     :     ","||","||","||","||","================","||     O","||     |","||    /|","||    /|\ ","||    / ","||    / \    *****GAMEOVER*****"]
letras = []
chutes = [""]
erros = 0
gameover = False

for i in range(len(palavra)) :
    letras.append(" _ ")

while gameover == False :
    print("\n")

    chute = input("Digite uma letra : ")
    for i in range(len(chutes)) :
        if chute == chutes[i] :
            print("\n")
            print("Digite outra letra pois esta já foi usada, meu chapa.")
            break
        else :
            chutes.append(chute)

    for i in range(len(palavra)) :
        if chute == palavra[i] :
            letras[i] = chute
        print(letras[i], " ", end="")

    if chute not in palavra :
        print("\n")
        erros += 1

    print("\n")
    if erros == 0 :
        for i in range(0, 7, 1):
            print(suicida[i])
    elif erros == 1 :
        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        for i in range(3, 7, 1):
            print(suicida[i])
    elif erros == 2 :
        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        print(suicida[8])
        for i in range(4, 7, 1):
            print(suicida[i])
    elif erros == 3 :
        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        print(suicida[9])
        for i in range(4, 7, 1):
            print(suicida[i])
    elif erros == 4 :
        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        print(suicida[10])
        for i in range(4, 7, 1):
            print(suicida[i])
    elif erros == 5 :
        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        print(suicida[10])
        print(suicida[11])
        for i in range(5, 7, 1):
            print(suicida[i])
    else :
        gameover = True

        for i in range(0, 2, 1):
            print(suicida[i])
        print(suicida[7])
        print(suicida[10])
        print(suicida[12])
        for i in range(5, 7, 1):
            print(suicida[i])

else :
    print("\n")
    print("A palavra secreta era '", palavra ,"'.")