def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        cvalue = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cvalue:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cvalue

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print("Sorted array is:", arr)