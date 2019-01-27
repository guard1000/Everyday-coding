def solution(n, results):
    answer = 0
    graph = [[0 for cols in range(n)] for rows in range(n)]
    for r in results:   #그래프 초기화
        graph[r[0]-1][r[1]-1] = 1
        graph[r[1]-1][r[0]-1] = -1
    for i in range(n):  #각 행별로 처리
        for j in range(n):
            if graph[i][j] == 1:
                for m in range(n):
                    if graph[j][m] == 1 and graph[i][m] == 0:
                        graph[i][m] = 1
                        graph[m][i] = -1
            elif graph[i][j] == -1:
                for m in range(n):
                    if graph[j][m] == -1 and graph[i][m] == 0:
                        graph[i][m] = -1
                        graph[m][i] = 1
    for i in range(n):
        if graph[i].count(0) == 1:
            answer += 1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))