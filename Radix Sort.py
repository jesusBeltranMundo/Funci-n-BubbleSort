#Autor J. Jesús Beltrán Mundo

def SeparaCadena (cad):
    A2=[]
    for j in cad:
        A2.append(j)
    return A2

def CreaLista2(k):
    L=[]
    for i in range(k+1):
        L.append([0]*2)
    return L

def CreaLista(k):
    L=[]
    for i in range(k+1):
        L.append(0)
    return L

def obtenerElemSinClaves(E):
    Elem=[]
    Elem.append("000000")
    for i in range(1,len(E)):
        Elem.append(E[i][0])
    return Elem

def CountingSort2(A,k):
    C=CreaLista(k)
    B=CreaLista2(len(A)-1)
    for j in range(1,len(A)):
        C[A[j][1]]=C[A[j][1]]+1
    for i in range (1,k+1):
        C[i]=C[i]+C[i-1]
    for j in range (len(A)-1,0,-1):
        B[ C[A[j][1]] ][1]=A[j][1]
        B[ C[A[j][1]] ][0]=A[j][0]
        C[A[j][1]]=C[A[j][1]]-1
    return B

def radixSort(A):
    numCar=(A[1])