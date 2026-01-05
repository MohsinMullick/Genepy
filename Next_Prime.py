import itertools
import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Start searching from the number just after 100,000,000
for num in itertools.count(100_000_001):
    if is_prime(num):
        print(num)
        sys.exit()