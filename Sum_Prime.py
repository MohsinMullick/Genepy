def sum_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i
    return total
print(sum_primes(10))

