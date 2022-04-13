import math

# https://app.codility.com/demo/results/trainingNM5VC3-V7V/
# 100% Pass, O(N)
def solution(K, A):
    curr_len = 0
    count = 0
    for i in A:
        if curr_len + i >= K:
            # print('i val:', i)
            count += 1
            curr_len = 0
        else:
            curr_len += i
    # print(count)
    return count


if __name__ == '__main__':
    K = 4
    A = [1, 2, 3, 4, 1, 1, 3]
    res = solution(K, A)
    print(res)
