def sum_of_divisors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    if n > 1:
        sum += n
    return sum

def is_friendly_pair(num1, num2):
    sum1 = sum_of_divisors(num1)
    sum2 = sum_of_divisors(num2)
    return sum1 / num1 == sum2 / num2

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if is_friendly_pair(num1, num2):
    print("Yes, they are a friendly pair")
else:
    print("No, they are not a friendly pair")