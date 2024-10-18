def is_kaprekar(n):
    if n == 1:
        return True
    square = str(n * n)
    for i in range(1, len(square)):
        left = int(square[:i])
        right = int(square[i:])
        if left + right == n:
            return True
    return False

# Test the function
num = int(input("Enter a number: "))
if is_kaprekar(num):
    print(num, "is a Kaprekar number.")
else:
    print(num, "is not a Kaprekar number.")