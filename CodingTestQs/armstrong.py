import math
def armstrong(n):
    sums, a = 0, 0
    var = n
    while var != 0:
        var //= 10
        a += 1
    var = n
    while var > 0:
        rem = var % 10
        sums += math.pow(rem, a)
        var //= 10
    if sums == n:
        return True
    else:
        return False
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
