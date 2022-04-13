def solution(A):
    l = len(A) + 1
    if 0 in A:
        l -= 1
    s = sum(A)
    a = l * (l + 1) // 2
    return a - s


if __name__ == "__main__":
    A = [3, 6, 2, 4, 1]
    m = solution(A)
    print(m)
