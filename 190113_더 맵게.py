import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >1:
        if scoville[0] >= K:
            return answer
        answer += 1
        tmp = scoville[0]
        heapq.heappop(scoville)
        tmp += (scoville[0]*2)
        heapq.heappop(scoville)
        heapq.heappush(scoville, tmp)

    if scoville[0] > K:
        return answer
    else:
        return -1

s=[1, 3, 2, 9, 10, 12]
k=7

print(solution(s,k))