print("******** JOGO DA FORCA ********")

chave = input("Digite a palavra secreta : ")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("********* INICIO **********")

acertos = []
chutes = [""]
erros = 0
final = False

for i in range(len(chave)):
    print("_ ", end = "")

print("\n")

while erros <= 6 and final == False :
    if erros == 0 :
        print("||=====:====")
        print("||     :     ")
        print("||")
        print("||")
        print("||")
        print("||")
        print("================")
    elif erros == 1 :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||")
        print("||")
        print("||")
        print("================")
    elif erros == 2 :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||     |")
        print("||")
        print("||")
        print("================")
    elif erros == 3 :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||    /|")
        print("||")
        print("||")
        print("================")
    elif erros == 4 :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||    /|\ ")
        print("||")
        print("||")
        print("================")
    elif erros == 5 :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||    /|\ ")
        print("||    / ")
        print("||")
        print("================")
    else :
        print("||=====:====")
        print("||     :     ")
        print("||     O")
        print("||    /|\ ")
        print("||    / \  ")
        print("||")
        print("================")

    chute = input("Digite uma letra : ")

    for i in range(len(chutes)) :
        if chute != chutes[i] :
            chutes.append(chute)
        else :
            print("\n")
            print("Você já usou esta letra, tente outra !! ")
            print("\n")

    for i in range(len(chave)):
        if chute == chave[i]:
            acertos.append(chute)
            print(chave[i], end="")
        else:
            print(" _ ", end="")

    print("\n")
else :
    print("acabou")
