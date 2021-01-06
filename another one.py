def is_prime(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return False if number <= 1 else True


n1 = 0
n2 = n1 + 1
n3 = n2 + 1
n4 = n3 + 1

numbers = [is_prime(n3), is_prime(n4)]

while not all(numbers):
    n1 += 1

print(numbers)