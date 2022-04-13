def solution(S):
    if len(S) == 0:
        return 1
    if S[0] == '}' or S[0] == ']' or S[0] == ')':
        return 0
    stack = []
    open_count = 0
    for c in S:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
            open_count += 1
        elif c == '}':
            open_count -= 1
            if len(stack) > 0 and stack.pop() != '{':
                return 0
        elif c == ']':
            open_count -= 1
            if len(stack) > 0 and stack.pop() != '[':
                return 0
        elif c == ')':
            open_count -= 1
            if len(stack) > 0 and stack.pop() != '(':
                return 0
    if len(stack) > 0:
        return 0
    if open_count < 0:
        return 0
    return 1


if __name__ == '__main__':
    S = '[[]]]]'
    success = solution(S)
    print(success)
