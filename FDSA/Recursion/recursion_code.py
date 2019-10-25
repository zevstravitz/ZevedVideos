
## MERGE SORT
def merge_sort(A):
    n = len(A)
    if n < 2:
        return
    mid = n // 2
    A1 = A[0:mid]
    A2 = A[mid:n]
    merge_sort(A1)
    merge_sort(A2)
    merge(A1, A2, A)

def merge(A1, A2, A):
    i=0
    j=0
    while i + j < len(A):
        if (i < len(A1) and A1[i] < A2[j]) or j == len(A2):
            A[i+j] = A1[i]
        else:
            A[i+j] = A2[j] 


