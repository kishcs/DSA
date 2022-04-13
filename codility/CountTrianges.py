def solution(A):
    A.sort()
    print(A)
    triangle_cnt = 0

    for p_idx in range(0, len(A) - 2):
        q_idx = p_idx + 1
        r_idx = p_idx + 2
        while r_idx < len(A):
            if A[p_idx] + A[q_idx] > A[r_idx]:
                triangle_cnt += r_idx - q_idx
                r_idx += 1
            elif q_idx < r_idx - 1:
                q_idx += 1
            else:
                r_idx += 1
                q_idx += 1

    return triangle_cnt


if __name__ == "__main__":
    A = [8, 9, 7, 9, 5] # => 10
    # A = [10, 2, 5, 1, 8, 12] # => 4
    # A = [1, 2, 3, 4, 5] # => 3
    dist = solution(A)
    print(dist)
