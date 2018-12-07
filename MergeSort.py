#Autor J. Jesús Beltrán Mundo

def CrearSubArreglo(self, A, indIzq, indDer):
    return A[inqIzq:indDer + 1]

def merge(self, A, p, q, r):
    z = mergeSort()
    Izq = z.CrearSubArreglo(A, q, r)
    Der = z.CrearSubArreglo(A, q+1, r)
    i = 0
    j = 0
    for k in range(p, r+1):
        if(j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i = i + 1
        else: 
            A[k] = Der[j]
            j = j + 1
def MergeSort(self, A, p, r):
    2 = mergeSort()
    if r - p > 0:
       q = int((p+r)/2)
       z.MergeSort(A, p, q)
       z.MergeSirt(A, q+1, r)
       z.MergeSort(A, p, q, r) 
