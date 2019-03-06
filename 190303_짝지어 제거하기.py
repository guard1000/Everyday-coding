#https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
#level 3

def solution(s):#stack
    stk=[s[0]]
    for i in range(1,len(s)):
        if len(stk) == 0 or s[i] != stk[-1]:
            stk.append(s[i])
        elif s[i] == stk[-1]:
            stk.pop()
    if len(stk) == 0:
        return 1
    return 0