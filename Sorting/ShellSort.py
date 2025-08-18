''' selects an element and compares element after a gap
similar to insertion sort. Insert selected element from the
gap at its proper position.
recompute gap until it becomes 0 - completes the shell sort.

Time Complexity is O(nlogn)
'''
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # initial gap
    while gap > 0:
        i = gap
        while i < n:
            # gvalue is holding the value to be inserted at proper position
            gvalue = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > gvalue:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = gvalue # insert the gvalue at its proper position
            i += 1
        gap //= 2
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    shell_sort(arr)
    print("Sorted array is:", arr)

