def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
primes = []

while count < 100:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

print("最初の30個の素数:", primes)