def mergeSort(A,l,r):
    if l < r:
        m = (l + r)//2
        mergeSort(A,l,m)
        mergeSort(A, m+1, r)
        merge(A,l,m,r)

def merge(A,l,m,r):
    i = l
    j =  m + 1
    k = l
    B = [0]*(r+1)
    while i <= m and j <= r:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i <= m:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= r:
        B[k]= A[j]
        j += 1
        k += 1
    for x in range(l, r+ 1):
        A[x] = B[x]
if __name__ == "__main__":
    A = [12, 11, 13, 5, 6, 7]
    print("Given array is", A)
    mergeSort(A, 0, len(A)-1)
    print("Sorted array is: ", A)   
# try and optimize the above code 
