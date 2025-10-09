def subseqequalssum(idx, arr, ds, n, target, sum=0):
    if idx == n:
        if sum == target:
            print(ds)
        return  # Ensure to return after processing the base case

    # Include the current element in the subsequence
    ds.append(arr[idx])
    sum += arr[idx]
    subseqequalssum(idx + 1, arr, ds, n, target, sum)

    # Backtrack and exclude the current element from the subsequence
    sum -= arr[idx]
    ds.pop()
    subseqequalssum(idx + 1, arr, ds, n, target, sum)


if __name__ == "__main__":
    arr = [3, 1, 2]
    ds = []
    n = len(arr)
    k = 3
    subseqequalssum(0, arr, ds, n, k, 0)