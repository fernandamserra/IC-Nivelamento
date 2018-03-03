def soma_lista(listinha):
    retorno = "error"
    if type(listinha) == type([]):
        retorno = 0
        for i in listinha:
            retorno+=i
    return retorno

def soma_matriz(matriz):
    

def pa(a1,r):
    retorno = []
    for i in range(20):
        retorno.append(a1+r*i)
    return retorno

def fat(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res
    '''
    if n<=1:
        return 1
    else:
        return n*fat(n-1)
    '''

print(soma_lista([]))

print(pa(1,2))

print(fat(5))
