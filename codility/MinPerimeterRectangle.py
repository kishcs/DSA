import sys


def solution(N):
    # if N == 1:
    #     return 4
    i = 1
    min_area = sys.maxsize
    while i*i <= N:
        if N % i == 0:
            l = N // i
            area = 2*l + 2*i
            if min_area > area:
                min_area = area
        i += 1
    return min_area


if __name__ == '__main__':
    N = 1;
    n = solution(N)
    print(n)
