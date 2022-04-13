import math


def prime_factors(n):
    primes = set()
    # Print the number of two's that divide n
    while n % 2 == 0:
        primes.add(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    till = int(math.sqrt(n)) + 1
    for i in range(3, till, 2):
        # while i divides n , print i and divide n
        while n % i == 0:
            primes.add(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes.add(int(n))
        # print(n)
    return sorted(primes)


if __name__ == '__main__':
    N = 112 # 2147483646
    p = prime_factors(N)
    print(p)

    # n = 100
    # for i in range(1, n, 2):
    #     print((i, n), end=' ')
    #     n = n/2