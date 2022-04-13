def solution(A):
    if len(A) == 0:
        return 0
    max_profit = 0
    bought = A[0]
    for i in range(1, len(A)):
        # print(bought, '==>', A[i])
        if A[i] > bought:
            if max_profit < A[i] - bought:
                max_profit = A[i] - bought
        else:
            bought = A[i]
    return max_profit


if __name__ == '__main__':
    # A = [4, 3, 8, 1, 5]
    # A = [23171, 21011, 21123, 21366, 21013, 21367]
    A = [9]
    profit = solution(A)
    print(profit)
    # print(21367-21011)


