def solution(A, B):
    # 0: upstream
    # 1: downstream
    alive = 0
    stack = []

    for i in range(len(A)):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                alive += 1
        else:
            stack.append(A[i])

    alive += len(stack)

    return alive


if __name__ == '__main__':
    A = [4, 3, 8, 1, 5]
    B = [0, 1, 0, 0, 0]     # [1, 1, 0, 1, 0]
    alive_count = solution(A, B)
    print(alive_count)
