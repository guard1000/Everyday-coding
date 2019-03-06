# https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3
# level 3
def solution(n, k):
    candi = [i for i in range(1,n+1)]
    answer = []
    k -= 1
    m = 1
    for i in range(1,n):
        m *= i
    for round in range(n-1):
        t = k//m
        tmp = candi.pop(int(t))
        answer.append(tmp)
        k = k%m
        m /= (n-1-round)
    answer.append(candi[0])
    return answer