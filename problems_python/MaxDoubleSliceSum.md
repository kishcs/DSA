A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].

#### Solution
- Create 2 arrays/list for left side sums and right side sums.
- left side sums list is for first slice. so it will have max sum upto a certain index.
- right side sums list is for second slice, it will have max sum from a certain index.
- A = [3, 2, 6, -1, 4, 5, -1, 2]
- LEFT: [0, 2, 8, 7, 11, 16, 15, 17]
- RIGHT: [19, 16, 14, 8, 9, 5, 0, 0]
- Then iterate for the central position between two lists.
- As central position will not be included in total sum, so we need to add prev value from LEFT list and next value from RIGHT list.

```
def solution(A):
    s = len(A)
    if s == 3:
        return 0
    left = [0] * s
    right = [0] * s

    for i in range(1, s):
        left[i] = max(0, A[i] + left[i-1])
    for i in range(s-1)[::-1]:
        # print(i, end=' ')
        right[i] = max(0, right[i+1] + A[i])
    # print(left, right)
    max_sum = 0
    for i in range(1, s-1):
        max_sum = max(max_sum, left[i-1] + right[i+1])
    return max_sum
```

https://rafal.io/posts/codility-max-double-slice-sum.html
