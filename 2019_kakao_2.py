# Nat = input().split()                   #나라 입력받음
# inp.append(list(input().split()))
# n, t, m, p = map(int, input().split())

def solution(N, stages):
    answer = []
    n = len(stages)
    result = [[0]*2 for z in range(N)]
    cnt1=0
    cnt2=0
    for i in range(1,N+1):  #실패율율 계산을 위한 자료정리
        for j in range(n):
            if stages[j] >= i:
                cnt1 = cnt1+1
            if stages[j] == i:
                cnt2 = cnt2+1
        if cnt1 == 0:
            result[i-1][1] = 0
        else:
            result[i-1][1] = cnt2/cnt1
        result[i-1][0] = i
        cnt1 = 0
        cnt2 = 0

    result = sorted(result, key=lambda x:x[1]) #1번 인덱스값을 기준으로 소팅

    for i in range(N-1):
        for j in range(i+1, N):
            if result[i][1] == result[j][1] and result[i][0] < result[j][0]:
                result[i], result[j] = result[j], result[i]
            else:
                break

    for i in range(N-1, -1, -1):
        answer.append(result[i][0])


    return answer

#
N=5
stages = [2,1,2,6,2,4,3,3]
print(solution(N, stages))
#