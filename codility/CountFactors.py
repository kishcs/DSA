def solution(N):
    if N == 1:
        return 1
    if N <= 3:
        return 2
    i = 1
    factors = 0
    while i*i < N:
        if N % i == 0:
            factors += 2
        i += 1
    if i*i == N:
        factors += 1
    return factors


if __name__ == '__main__':
    N = 4;
    n = solution(N)
    print(n)
