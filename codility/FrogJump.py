import math


def solution(X, Y, D):
    diff = Y - X
    print('diff:', diff)
    if diff == 0:
        return 0
    jumps = diff / D
    print('jumps:', jumps)
    jump = math.ceil(jumps)
    print('jump:', jump)
    return jump


def main():
    jump = solution(1, 1000000000, 2)
    print(jump)


if __name__ == "__main__":
    main()
