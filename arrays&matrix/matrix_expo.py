from typing import List

# Type alias for readability
Matrix = List[List[float]]

def power_number(x: float, k: int) -> float:
    ret = 1.0
    while k > 0:
        if k & 1:
            ret *= x
        x *= x
        k >>= 1
    return ret


def multiply(A: Matrix, B: Matrix) -> Matrix:
    n, m, k = len(A), len(A[0]), len(B[0])
    C = [[0.0 for _ in range(k)] for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for l in range(m):
                C[i][j] += A[i][l] * B[l][j]
    
    return C


def power_matrix(A: Matrix, k: int) -> Matrix:
    n = len(A)
    
    # Identity matrix
    ret = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1.0
    
    B = [row[:] for row in A]  # Copy of A
    
    while k > 0:
        if k & 1:
            ret = multiply(ret, B)
        B = multiply(B, B)
        k >>= 1
    
    return ret


def main():
    # Expected Output:
    # 2.37^48 = 9.72569e+17
    # Matrix output...

    n = 2.37
    k = 48
    print(f"{n}^{k} = {power_number(n, k)}")

    At = [
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]
    ]

    A = [[float(At[i][j]) for j in range(5)] for i in range(5)]
    Ap = power_matrix(A, k)

    print()
    for row in Ap:
        print(" ".join(str(int(x)) if x.is_integer() else str(x) for x in row))


if __name__ == "__main__":
    main()