def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for div in range(int(num**0.5)+1, 1, -1):
        if num % div == 0:
            return False

    return True


num = 600851475143

for i_divider in range(int(num**0.5)+1, 1, -1):
    if num % i_divider == 0 and is_prime(i_divider):
        print(i_divider)
        break
