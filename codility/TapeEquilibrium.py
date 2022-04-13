def solution(A):
    s = sum(A)
    local_sum = 0
    final_min = 100000000
    for i in A[:-1]:
        local_sum += i
        curr_min = abs((s - local_sum) - local_sum)
        if final_min > curr_min:
            final_min = curr_min
    return final_min


if __name__ == "__main__":
    arr = [3, 1000, -999]
    low = solution(arr)
    print(low)
