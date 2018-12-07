#Autor J. Jesús Beltrán Mundo

def CreaLista(k):
    L=[]
    for i in range(k+1):
        L.append(0)
    return L

def CountingSort(A,k):
    C=CreaLista(k)
    B=CreaLista(len(A)-1)
    for j in range