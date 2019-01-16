import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    n = len(dates)
    i=0
    tmp=[]
    while (stock < k):
        while (i < n and dates[i] <= stock):
            tmp.append(supplies[i])
            i += 1
        answer += 1
        stock += max(tmp)
        tmp.remove(max(tmp))

    return answer


s=4
d=[4,10,15]
su=[20,5,10]
k=30

print(solution(s,d,su,k))