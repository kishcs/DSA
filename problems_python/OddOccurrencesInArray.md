A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

```
def solution(A):
    store = {}
    target = []

    # Third way -- Timeout Error
    # for i in A:
    #     if A.count(i) % 2 != 0:
    #         return i

    # Second way -- Timeout Error
    # for i in A:
    #     count = store.get(i, 0)
    #     store[i] = count + 1
    #     if (count + 1) % 2 != 0:
    #         target.append(i)
    #     else:
    #         target.remove(i)
    # print(store)
    # return target[0]

    # First way -- Passed O(N) or O(N*log(N))
    for i in A:
        count = store.get(i, 0)
        store[i] = count + 1

    # for k, v in map.items():
    #     if v % 2 != 0:
    #         return k

    # val = [k for k, v in sorted(store.items(), key=lambda item: item[1]) if v % 2 != 0]
    val = [k for k, v in sorted(store.items()) if v % 2 != 0]
    return val[0]


def main():
    A = [9, 3, 9, 4, 3, 4, 7, 5, 7, 5, 7, 7, 9, 7, 9]
    odd = solution(A)
    print(odd)


if __name__ == "__main__":
    main()
```
