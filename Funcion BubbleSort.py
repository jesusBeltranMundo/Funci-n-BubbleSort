#Autor J. Jesús Beltrán Mundo

def bubbleSort(A):
    for i in range(1,len(A)):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
		A[j] = A[j+1]
		A[j+1] = temp


#funcion BubbleSort Mejorada


def bubbleSort2(A):
    bandera= True
    pasada=0
    while pasada < len(A)-1 and bandera:
        bandera=False
        for j in range(len(A)-1):
            if(A[j] > A[j+1] ):
                bandera=True
                temp = A[j]
		A[j] = A[j+1]
		A[j+1] = temp
        pasada = pasada+1
