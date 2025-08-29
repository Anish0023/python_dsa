def quicksort(A,l,h):
    if l < h:
        p = partition(A,l,h)
        quicksort(A,l,p-1)
        quicksort(A,p+1,h)
def partition(A,l,h):
    pivot  = A[l]
    i = l + 1
    j = h
    while True:
        while i <=j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[l], A[j] = A[j], A[l]
    return j
if __name__ == "__main__":
    A = [12, 11, 13, 5, 6, 7]
    print("Given array is", A)
    quicksort(A, 0, len(A)-1)
    print("Sorted array is: ", A)