# https://app.codility.com/demo/results/trainingCWXWSC-A5K/
# 40% Wrong Answer
def solution(M, A):
    N = len(A)
    if N == 1:
        return 1

    start = 0
    dist = 0
    for i in range(N):
        # print('for', i)
        if i + 1 < N:
            if A[i] == A[i + 1]:
                # calculate for i
                elements = (i - start) + 1
                dist += (elements * (elements + 1)) / 2
                start = i + 1
        else:
            # print('last', i)
            elements = (i - start) + 1
            dist += (elements * (elements + 1)) / 2
    return int(dist) if int(dist) <= 1000000000 else 1000000000


# https://app.codility.com/demo/results/trainingGUT8XZ-XBY/
# 100% Pass O(N)
def solution1(M, A):
    the_sum = 0
    front = back = 0
    seen = [False] * (M + 1)
    while front < len(A) and back < len(A):
        while front < len(A) and seen[A[front]] != True:
            the_sum += (front - back + 1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1

            seen[A[back]] = False
            back += 1

    return min(the_sum, 1000000000)


if __name__ == "__main__":
    M = 10
    A = [8, 9, 7, 9, 5]
    dist = solution1(M, A)
    print(dist)

'''
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(M, A) {
  // write your code in JavaScript (Node.js 8.9.4)
  const memory = new Set();
  let count = 0;
  let tail = 0;

  for (let i = 0; i < A.length; i++) {
    if (!memory.has(A[i])) {
      memory.add(A[i]);
      continue;
    }
    count += slices(i - tail);
    while (A[tail] !== A[i]) {
      memory.delete(A[tail]);
      tail++;
    }
    tail++;
    count -= slices(i - tail);
  }
  count += slices(A.length - tail);
  return Math.min(count, 1000000000);
}

function slices(n) {
  return n * (n + 1) / 2;
}
'''
