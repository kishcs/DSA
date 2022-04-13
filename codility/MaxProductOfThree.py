def solution(A):
    A.sort()
    sol1 = A[-1] * A[-2] * A[-3]
    sol2 = A[0]*A[1]*A[-1]
    print(sol1, sol2)
    return sol1 if sol1 > sol2 else sol2


if __name__ == '__main__':
    arr = [-5, 5, -5, 4]
    pos = solution(arr)
    print(pos)