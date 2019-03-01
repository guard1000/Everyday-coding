# https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3
# level3
def solution(n):
    a,b,c=1,2,0
    if n < 3:   return n
    for i in range(3,n+1):
        c = b
        b = (a+b)%1234567
        a =c
    return b