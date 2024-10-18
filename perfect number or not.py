def sum_of_divisors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

def is_perfect_number(n):
    return sum_of_divisors(n) == n

# Test the function
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("Yes, it is a perfect number")
else:
    print("No, it is not a perfect number")