def counting1(A, m):
    count = [0] * (m + 1)
    for k in A:
        count[k] += 1
    return count


def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    print('Sum(A):', sum_a, 'Sum(B):', sum_b, 'Diff:', d)
    if d % 2 == 1:
        return False
    d //= 2
    print('Diff now:', d)
    count = counting(A, m)
    print('count array:', count)
    for i in range(n):
        if 0 <= B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False


if __name__ == "__main__":
    m = 5
    A = [5, 1, 4, 3, 2, 1, 3, 1, 4, 5]
    B = [5, 3, 4, 3, 6, 1, 3, 1, 4, 5]
    # c = counting(A, m)
    # print(c)
    # print(sum(A), sum(B))
    stat = fast_solution(A, B, 6)
    print(stat)