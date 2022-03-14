import random

def partition(A, start, stop):
    pivot = A[stop]
    i = start
    for j in range(start, stop):
        if A[j] <= pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i+=1
    temp = A[i]
    A[i] = A[stop]
    A[stop] = temp
    return i

def qsort(A, start, stop):
    if start < stop:
        p = partition(A, start, stop)
        qsort(A, start, p - 1)
        qsort(A, p + 1, stop)
        
for x in range(0, 10) :
    L = [random.randint(0, 100) for k in range(0,10)] 
    print("Quick Sort Input:", L)
    qsort (L, 0, len(L) - 1) 
    print("Result After Quick Sort:", L)
