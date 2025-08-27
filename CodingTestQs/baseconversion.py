def conversion(num,base):
    rem = num % base
    if num == 0:
        return 0
    conversion(num // base, base)
    if rem < 10:
        print(rem, end = '')
    else:
        print(chr(rem - 10 + ord('A')), end = '')
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    base = int(input("Enter the base to convert to (2-16): "))
    if base < 2 or base > 16:
        print("Base must be between 2 and 16")
    else:
        print(f"Number {num} in base {base} is: ", end = '')
        conversion(num, base)
        print()