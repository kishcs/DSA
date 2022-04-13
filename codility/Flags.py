import math


# Java Sol : https://app.codility.com/demo/results/trainingMQSRG2-XDP/
# https://app.codility.com/demo/results/trainingPFZRDD-6NN/
# 100% Pass
def solution(A):
    s = len(A)
    if s < 3:
        return 0
    peaks = []
    total_peaks = 0
    for i in range(1, s-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
            total_peaks += 1

    # print(total_peaks, len(peaks)-1)

    if total_peaks <= 1:
        return total_peaks

    max_flags = math.ceil(math.sqrt(peaks[total_peaks-1] - peaks[0]))
    for flag in range(max_flags, 1, -1):
        start_index = 0
        end_index = total_peaks-1
        start_flag = peaks[start_index]
        end_flag = peaks[end_index]
        flag_count = 2
        while start_index < end_index:
            start_index += 1
            end_index -= 1
            if start_flag + flag <= peaks[start_index] <= end_flag - flag:
                flag_count += 1
                start_flag = peaks[start_index]
            if start_flag + flag <= peaks[end_index] <= end_flag - flag:
                flag_count += 1
                end_flag = peaks[end_index]

            if flag_count == flag:
                return flag
    return 0
    '''
    for n in range(total_peaks, 0, -1):
        for i in range(1, total_peaks):
            if peaks[i] >= first_flag + n:
                count += 1
                first_flag = peaks[i]
        # print("flags:", count)
        if n == count:
            return count
    '''

def create_peaks(A):
    N = len(A)
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks[i] = True
    return peaks


def check(A):
    N = len(A)
    peaks = create_peaks(A)
    max_flags = peaks.count(True)
    for x in range(max_flags, 0, -1):
        flags = x
        pos = 0
        while pos < N and flags > 0:
            if peaks[pos]:
                flags -= 1
                pos += x
            else:
                pos += 1
        if flags == 0:
            return x


if __name__ == '__main__':
    A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    n = check(A)
    print(n)
    n = solution(A)
    print(n)

    # for i in range(4, 0, -1):
    #     print(i)

    # for i in range(1, 5)[::-1]:
    #     print(i, end=' ')
    # print()
    # for i in range(4, 0, -1):
    #     print(i, end=' ')