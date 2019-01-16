def dijkstra(graph, visit, answer,m):
    if len(visit) == len(graph):
        return answer
    cost = m

    for i in visit:
        for j in range(len(graph[i])):
            if graph[i][j] < cost and j not in visit:
                cost = graph[i][j]
                y = j
    answer += cost
    visit.append(y)
    return dijkstra(graph, visit, answer, m)

def solution(n, costs):
    #다익스트라
    answer = 0
    visit=[]
    costs = sorted(costs, key=lambda x: x[2])
    m = costs[len(costs)-1][2]+1    ##costs 중 제일 큰거보다 1 큰 값으로 초기화할때 씀

    #graph 만들기
    graph = [[m for rows in range(n)] for cols in range(n)]
    for i in costs:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]

    visit.append(costs[0][0])
    visit.append(costs[0][1])
    answer += costs[0][2]
    answer = dijkstra(graph, visit, answer, m)
    return answer

c = [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]]
print(solution(4,c))