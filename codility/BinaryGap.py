def solution(number):
    b = bin(number)
    b = b[2:]
    print(b)
    max_gap = 0
    curr_gap = 0
    for i in str(b):
        if i == str(1):
            if max_gap < curr_gap:
                max_gap = curr_gap
            curr_gap = 0
        else:
            curr_gap += 1
    return max_gap


def main():
    # 8000001 --> 8
    # 805306373 --> 25
    # 2147483647 --> 0
    gap = solution(805306373)
    print(gap)


if __name__ == "__main__":
    main()
