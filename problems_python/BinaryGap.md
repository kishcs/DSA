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
