def bubble_sort(arr):
    n = len(arr)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array is:", arr)