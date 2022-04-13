def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in range(n):
        # print('back->', back)
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        # print(total, front)
        if total == s:
            return True
        total -= A[back]
        # print(total)


if __name__ == '__main__':
    s = 12
    A = [6, 2, 7, 4, 1, 3, 6]
    stat = caterpillarMethod(A, s)
    print(stat)
