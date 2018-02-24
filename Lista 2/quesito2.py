mes = input("Digite o nome de um mês :")

aux = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
numero = 0
i = 0

while i < 12:
    if mes == aux[i]:
        numero = i + 1
        print("Mês ", numero)
    i = i + 1
else:
    if numero == 0 :
        print("Entrada inválida")