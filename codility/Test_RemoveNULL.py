import re


def solution(S):
    arr = S.split('\n')
    print(arr)
    # output = list()
    output = arr[0] + '\n'
    # j = 1
    for i in range(1, len(arr)):
        # f = arr[i].find(',NULL,')
        # print(f)
        print(arr[i], '=>', re.search(r"\b" + 'NULL' + r"\b", arr[i]))
        if not re.search(r'\b' + 'NULL' + r'\b', arr[i]):
            output += arr[i] + '\n'
    print('-'*20)
    print(output.strip('\n'))

    return 1000


if __name__ == "__main__":
    # s = 'head,header,x,y,z\nabc,def,56,ANULLAT,null\nNULL,sdsds,1,2,3' \
    #     '\nasdasda,NULL,3,4,5\n1,2,ANULL,4,5\n1,2,3,4,NULL'
    s = 'head,header,x,y,z\n' \
        'asdasda,_NULL,3,NULLS,5\n1,2,ANULL,4,.NULL\n1,2,IS NULL VAL,4,5'
    op = solution(s)
    print(op)
