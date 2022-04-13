#!/usr/bin/env python

if __name__ == "__main__":
    s = 'MALAYBYALAM'
    if s == s[::-1]:
        print(s,'is PALINDROME')
    else:
        print(s, 'IS NOT PALINDROME')

    l = len(s)//2
    print(s[:l], s[-l:])
    if s[:l][::-1] == s[-l:]:
        print('Palindrome')
    else:
        print('not Palindrome')

