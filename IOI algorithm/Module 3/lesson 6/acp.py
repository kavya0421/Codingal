
print("Two-digit prime numbers:")

for number in range(10, 100):
    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
