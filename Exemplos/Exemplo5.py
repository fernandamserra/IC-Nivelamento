v = int(input("Digite a velocidade do veículo(km/h) :"))

if v > 60 :
    aux = 200 + (v - 60)* 3
    print("Multa de", aux , "golpes.")
else :
    print("Não há multa !")