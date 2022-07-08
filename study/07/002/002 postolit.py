num = 600851475143
divisors = []
for i in range(1, int(num**0.5)+1):
    is_prime = 0
    if num % i == 0:
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                is_prime += 1
            if is_prime == 0:
                divisors.append(i)
print(max(divisors))
