def solution(N, A):     # 88% Pass
    # counters = [0 for x in range(N)]
    counters = [0] * N
    repeat = N+1
    # print(counters)
    max_counter = 0
    for i in A:
        # print('got', i, 'counters:', counters, 'max_counter', max_counter)
        if i != repeat:
            counters[i-1] += 1
            if max_counter < counters[i-1]:
                max_counter = counters[i-1]
        else:
            # counters = [max_counter for x in range(N)]
            counters = [max_counter] * N
    return counters


if __name__ == '__main__':
    N = 1000
    A = [3, 4, 3, 1001, 6, 1, 4, 4, 123, 23]
    final_counters = solution(N, A)
    print(final_counters)

'''
#include <algorithm>
 
vector<int> solution(int N, vector<int> &A) {
    vector<int> sol;
    int current_max = 0;
    int last_increase = 0;
 
    for(int i=0; i<N;i++){
        sol.push_back(0);
    }
 
    for(unsigned int i=0; i<A.size();i++){
        if (A[i] > N) {
            last_increase = current_max;
        } else {
            sol[A[i]-1] = max(sol[A[i]-1], last_increase);
            sol[A[i]-1]++;
            current_max = max(current_max, sol[A[i]-1]);
        }
    }
 
    for(int i=0; i<N;i++){
        sol[i] = max(sol[i], last_increase);
    }
 
    return sol;
}
'''