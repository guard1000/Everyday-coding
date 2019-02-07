'''
def solution(n, works):
    answer=0
    if sum(works) <= n:
        return 0
    if len(works) == 1:
        return (works[0]-n)**2
    works = sorted(works, reverse=True)
    while n > 0:
        n -= 1
        i = works.index(max(works))
        works[i] -= 1
    for i in works:
        answer += i**2
    return answer
'''

def solution(n, works):
    answer=0
    if sum(works) <= n:
        return 0
    if len(works) == 1:
        return (works[0]-n)**2
    works = sorted(works, reverse=True)
    i = 0
    while n-i-1 >0 :
        if works[i] == works[i+1]:
            i += 1
        else:
            n = n-i-1
            for j in range(i+1):
                works[j] -= 1
    works = sorted(works,reverse=True)
    for i in range(n):
        works[i] -= 1
    for i in works:
        answer += i**2
    return answer

print(solution(4,[4, 3, 3]))
print(solution(1,[2, 1, 2]))