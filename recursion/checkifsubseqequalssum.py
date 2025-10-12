def checkSubseqEqualSum(idx, arr,ds, n, target, sum=0):
    if idx == n:
        if target == sum:
            print(ds)
            return True
        return False
    ds.append(arr[idx])
    sum += arr[idx]
    if checkSubseqEqualSum(idx + 1, arr, ds, n, target, sum):
        return True
    #minimizing the recurison calls  as we just need to find one subsequence
    sum -= arr[idx]
    ds.pop()
    if checkSubseqEqualSum(idx + 1, arr, ds, n, target, sum):
        return True
    return False
if __name__ == "__main__":
    arr = [3, 1, 2]
    ds = []
    n = len(arr)
    k = 6
    if not checkSubseqEqualSum(0, arr, ds, n, k, 0):
        print("No subsequence found with sum =", k)