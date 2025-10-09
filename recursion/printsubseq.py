def subseq(idx, ds, arr, n):
    if idx == n:
        print(ds)
        return
    ds.append(arr[idx])
    subseq(idx+1,ds,arr,n)
    ds.pop()
    subseq(idx+1,ds,arr,n)

if __name__ == "__main__":
    arr= [3, 1, 2]
    n = len(arr)
    ds = []
    subseq(0, ds, arr, n)