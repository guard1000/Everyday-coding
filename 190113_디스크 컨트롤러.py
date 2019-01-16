#작업시간은 고정이므로, 평균대기시간을 최소화 시킨다.
#SJF 스케줄링
import heapq

def solution(jobs):
    answer = 0
    t=0
    wait=[]
    heapq.heapify(jobs)
    n = len(jobs)
    cnt = 0

    hap=0
    for i in jobs:
        hap += i[1]

    heapq.heapify(wait)
    # SJF 대기시간 계산

    while cnt < n:
        while len(jobs) > 0 and jobs[0][0] <= t:
            heapq.heappush(wait, [jobs[0][1],jobs[0][0]])
            heapq.heappop(jobs)

        if len(wait) > 0:
            answer += (t-wait[0][1])
            t += wait[0][0]
            heapq.heappop(wait)

        else:
            t = jobs[0][0] +jobs[0][1]
            heapq.heappop(jobs)
        cnt += 1
    answer += hap
    return answer//n


'''
def solution(jobs):
    answer = 0
    t=0
    wait=[]
    jobs = sorted(jobs, key=lambda x: x[0])
    n = len(jobs)
    cnt = 0
    i = 0

    # SJF 대기시간 계산
    while cnt < n:
        #wait 리스트 추가
        while i < n and jobs[i][0] <= t:
            wait.append(jobs[i])
            i += 1

        #만약 wait 리스트가 없다면? -> 바로 i 가 가리키는 녀석이 들어오며 실행
        if len(wait) == 0:
            t = jobs[i][0] + jobs[i][1]
            i += 1
        else:
            wn = len(wait)
            nxt = 0
            tmp = wait[0][1]
            for j in range(wn):
                if wait[j][1] <= tmp:
                    tmp = wait[j][1]
                    nxt = j
            answer += (t-wait[nxt][0])
            t += wait[nxt][1]
            wait.pop(nxt)
        cnt += 1
    for x in range(n):
        answer += jobs[x][1]
    return answer//n
'''

j =[[0, 3], [1, 9], [2, 6]]
j2 = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
print(solution(j))
print(solution(j2))