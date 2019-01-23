def solution(K, travel):
    answer = 0
    n = len(travel)
    for i in range(n):
        K -= travel[i][2]
        answer += travel[i][3]
        travel[i][0] -= travel[i][2]
        travel[i][1] -= travel[i][3]
    arr=[[0 for cols in range(K+1)] for rows in range(n+1)]
    for i in range(n+1):
        for w in range(K+1):
            if i ==0 or w ==0:
                arr[i][w] = 0
            elif travel[i-1][0] <= w:
                arr[i][w] = max(travel[i-1][1] + arr[i-1][w-travel[i-1][0]], arr[i-1][w])
            else:
                arr[i][w] = arr[i-1][w]
    return answer+arr[n][K]



'''
#재귀로 하려니까 시간초과 오질라게 뜸
def knapsack(K, idx, n, travel):
    if idx == n:
        return 0
    #가져가지 않음
    unselect = knapsack(K, idx+1, n, travel)
    select = 0
    #가져감
    if K >= travel[idx][0]:
        select =knapsack(K-travel[idx][0], idx+1, n, travel) + travel[idx][1]
    return max(unselect, select)


def solution(K, travel):
    answer = 0
    n = len(travel)
    for i in range(n):
        K -= travel[i][2]
        answer += travel[i][3]
        travel[i][0] -= travel[i][2]
        travel[i][1] -= travel[i][3]
    return answer+knapsack(K, 0, n, travel)
'''


#도보시간 - 도보 모금액 - 자전거 시간 - 자전거 모금액
print(solution(1650,[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))
print(solution(3000,[[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))
