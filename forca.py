print("******** JOGO DA FORCA ********")
palavra = input("Digite a palavra secreta : ")

for i in range(10) :
    print("\n")

print("********* INICIO **********")

letras = []
chutes = [""]
erros = 0

for i in range(len(palavra)) :
    letras.append(" _ ")

gameover = False
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
        print("Você agora possui ", erros ,"/6 erros.")

    if erros == 6 :
        gameover = True

else :
    print("this shit is over")
    print("A palavra secreta era '", palavra ,"'.")