import itertools    #모든 조합을 위해!

def solution(numbers, target):
    answer = 0
    asum=0
    alist=[]
    goal = sum(numbers)-target
    for i in range(len(numbers)):
        alist.append(i)
    for j in range(len(numbers)):
        mypermutation = itertools.combinations(alist,j+1)
        for s in mypermutation:                         #각 조합에서의 모든 경우에서
            for k in s:
                asum = asum + numbers[k]*2
            if asum == goal:
                answer = answer + 1
            asum=0
    return answer

print(solution([1,1,1,1,1],3))