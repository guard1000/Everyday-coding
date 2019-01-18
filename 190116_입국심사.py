def bsearch(s,e,times,n):
    if s == e:
        return s
    m = (s+e)//2
    if m == s:
        return m+1

    tmp = sum([m//i for i in times])
    if tmp > n:
        return bsearch(s,m,times,n)
    elif tmp < n:
        return bsearch(m,e,times,n)
    elif sum([(m-1)//i for i in times]) == tmp: #그 중에서 최저 찾아야 해
        return bsearch(s,m-1,times,n)

    else:
        return m

def solution(n, times):
    return bsearch(1,max(times)*n,times,n)

n = 6
times = [7,10]
print(solution(n,times))
print(solution(6, [6,10]))
print(solution(6, [8,10]))
print(solution(6, [4,10]))
print(solution(11, [3,4,10]))
print(solution(5, [1,1,10]))