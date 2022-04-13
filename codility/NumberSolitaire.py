def solution(A):
    """
    https://app.codility.com/demo/results/trainingG5FNV9-7SY/
    On any square ask, what is the best exit score from any of the previous 6
    squares that I can be reached from? And what wil me exit score be?

          +-----------------------------------------------+
    entry | 0 | 0 | 0 | 0 | 0 | 0 | 0 |-2 |-4 | -4| 5 | 5 |
    ------+-----------------------------------------------+
    value | 0 |-2 |-9 |-9 |-9 |-9 |-9 |-2 |-2 | 9 | 0 |-2 |
    ------+-----------------------------------------------+
    exit  | 0 |-2 |-9 |-9 |-9 |-9 |-9 |-4 |-6 | 5 | 5 | 3 |
    ------+-----------------------------------------------+
    """
    n = len(A)
    rolls = 6  # 6 sided dice means we can look back a max of 6 spaces.
    exit_score = [A[0]] * n  # Set all exit scores to start score
    print(exit_score)
    for i in range(1, n):
        # At each point slice the previous 6 exit scores and choose the best
        spread = exit_score[max(i - rolls, 0):i]
        # print(spread, max(spread))
        exit_score[i] = A[i] + max(spread)
    return exit_score[-1]


if __name__ == '__main__':
    arr = [1, -2, 0, 9, -1, -2]  # => 8
    arr = [1, 2, 3, 2, 5, 3, 1]  # => 17
    arr = [5, -1, -2, -1, -2, -3, -2, 3]  # => 7
    arr = [1, -1, -2, -1, -1, -1, -2, -1, -2, 5, 3, 1]  # => 9
    max_count = solution(arr)
    print(max_count)
