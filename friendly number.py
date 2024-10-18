def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sum_of_proper_divisors(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

def are_friendly(a, b):
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_friendly(num1, num2):
    print(num1, "and", num2, "are friendly numbers.")
else:
    print(num1, "and", num2, "are not friendly numbers.")