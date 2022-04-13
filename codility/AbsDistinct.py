# https://app.codility.com/demo/results/trainingSSTXHW-G7V/
# 100%
# O(N) or O(N*log(N))
def solution(A):
    l = [abs(i) for i in A]
    # s = set(l)
    return len(set(l))


if __name__ == "__main__":
    A = [-5, -3, -1, 0, 3, 6]
    dist = solution(A)
    print(dist)