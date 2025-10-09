def countSubseqEqualSum(idx, arr, n, target, sum=0):
    if idx == n:
        if sum == target:
            return 1  # Found a valid subsequence
        return 0  # No valid subsequence

    # Include the current element in the subsequence
    sum += arr[idx]
    count_with = countSubseqEqualSum(idx + 1, arr, n, target, sum)

    # Backtrack and exclude the current element from the subsequence
    sum -= arr[idx]
    count_without = countSubseqEqualSum(idx + 1, arr, n, target, sum)

    # Return the total count
    return count_with + count_without


if __name__ == "__main__":
    arr = [3, 1, 2]
    n = len(arr)
    k = 3
    result = countSubseqEqualSum(0, arr, n, k, 0)
    print("Number of subsequences with sum =", k, "is:", result)