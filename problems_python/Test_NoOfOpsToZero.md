S = '00011100' => 28

Two operations can be performed on the number.
- if number is even, divide it by 2
- if number is odd, reduce 1 from it.
Continue operations till it becomes zero.

1. 28 -> even -> 28/2
2. 14 -> even -> 14/2
3. 7 -> odd -> 7-1
4. 6 -> even -> 6/2
5. 3 -> odd -> 3-1
6. 2 -> even -> 2/2
7. 1 -> odd -> 1-1
-> number becomes zero

So 7 operations required for 28 till 0.
- Answer is 7.

Similarly for S = '1' * 400000, answer woule be 799999

```
def solution(S)
  a = int(S, 2)
  ops = 0
  while a:
    if 1 < a and a & 1:
      ops += 1
    a >>= 1
    ops += 1
  return ops

if __name__ == '__main__':
  S = '00011100' # 28
  op = solution(S)
  print(op) # should return 7
```
