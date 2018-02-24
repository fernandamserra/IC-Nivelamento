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

corpo = [0,1,2,3,4,5]
letras = []
chutes = []
erros = 0

while erros <= 6 or letras == len(chave) :
    chute = input("Digite uma letra : ")
    for i in range(len(chave)) :
        if chute == chave[i] :
            chutes.append(chute)
        else:
            erros += 1
else :
    print("rsrs")

