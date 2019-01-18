def func(a,b,N):
    c = a+b
    N -= 1
    if N == 0:
        return 2*(c+b)+2*c
    return func(b,c,N)

def solution(N):
    if N == 1: return 4
    if N == 2: return 6
    return func(1,1,N-2)

print(solution(5))
print(solution(6))