
# https://app.codility.com/demo/results/trainingYDY52R-EP5/
# 100% Pass, O(N)
def solution(A, B):
    n = len(A)
    if n <= 1:
        return n
    count = 1
    end = B[0]
    for i in range(1, n):
        if A[i] > end:
            count += 1
            end = B[i]
    return count


if __name__ == '__main__':
    A = [1, 3, 7, 9, 9]
    B = [5, 6, 8, 9, 10]
    res = solution(A, B)
    print(res)
