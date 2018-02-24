L = [45,23,31,90,1,10,78,134,0]
aux = 0

for i in range(len(L)) :
    if L[i] > L[i + 1] :
        aux = L[i + 1]
        L[i + 1] = L[i]
        L[i] = aux
print(L)