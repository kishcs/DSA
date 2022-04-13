def solution(N, M):
    keep = set()
    i = 0
    while i not in keep and i < N:
        keep.add(i)
        i = (i + M) % N
    return len(keep)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(A, B):
    return (A * B) / gcd(A, B)


def solution2(N, M):
    return lcm(N, M) / M


if __name__ == '__main__':
    N = 947853000
    M = 453658
    print('Faster=>', solution2(N, M))
    ate = solution(N, M)
    print(ate)
