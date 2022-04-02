Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

### Optimized Solution
```
def solution(A, B, K):
    if K > B:
        return 0
     
    count = 0
    first = -1
    if A % K == 0:
        first = A
    else:
        rem = A % K
        first = A + K - rem
    # print('FIRST', first)
    # for i in range(A, B+1):
    #     if i % K == 0:
    #         first = i
    #         break
    last = K * (B // K)
    #print(first, 'and', last)
    #print(first // K, 'and', last // K)

    # if first == -1:
    #     return 0
    count = (last//K) - (first//K) + 1
    #print('==>', checkthis)
    #count = len([i for i in range(first, last+1, K)])
    return count
```

### TimeOut Solution
```
def solution(A, B, K):
    # write your code in Python 3.6
    count = 0
    first = -1
    for i in range(A, B+1):
        if i % K == 0:
            first = i
            break
            # count += 1
    # print(first)
    if first == -1:
        return 0
    count = len([i for i in range(first, B+1, K)])
    return count
```
