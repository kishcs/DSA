def solution(S, P, Q):
    book = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    N = [book[s] for s in S]
    # print(N)
    M = len(P)
    min_seq = []
    for i in range(M):
        # min_seq.append(sorted(N[P[i]:Q[i]+1])[0])
        # min_seq.append(min(N[P[i]:Q[i] + 1]))
        min_seq += [min(N[P[i]:Q[i] + 1])]
    return min_seq


def solution1(S, P, Q):     #62% Pass
    book = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    M = len(P)
    min_seq = []
    for i in range(M):
        min_seq += [book[min(S[P[i]:Q[i] + 1])]]
    return min_seq


def giveNum(string):
    if 'A' in string:
        return 1
    elif 'C' in string:
        return 2
    elif 'G' in string:
        return 3
    else:
        return 4


def solution2(S, P, Q):     #100% Pass
    # book = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    M = len(P)
    min_seq = []
    for i in range(M):
        # min_seq += [book[min(S[P[i]:Q[i] + 1])]]
        min_seq += [giveNum(S[P[i]:Q[i] + 1])]
    return min_seq


if __name__ == '__main__':
    # S = 'CAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTACAGCCTA'
    S = 'CGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
    P = [2, 3, 0]
    Q = [30, 20, len(S)]
    min_impact = solution2(S, P, Q)
    print(min_impact)
    print(min(S), set(S), min(set(S)))
