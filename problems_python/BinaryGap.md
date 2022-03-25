# Max Binary Gap in any number.

```
def binaryGap(num):
    b = bin(num)
    b = b[2:]
    print(b)
    count = 0
    maxGap = 0
    for i in b:
        if(int(i) == 1):
            if(count > 0):
                if(maxGap < count):
                    maxGap = count
                count = 0
        else:
            count += 1
    print("max binary gap:", maxGap)
```


# Full Program

```
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
    gap = solution(800001)
    print(gap)


if __name__ == "__main__":
    main()

```
