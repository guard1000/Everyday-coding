import sys
def dijkstra(K, V, graph):
    INF = sys.maxsize
    s = [False] * V
    d = [INF] * V
    d[K - 1] = 0

    while True:
        m = INF
        N = -1
        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
        if m == INF:
            break
        s[N] = True
        for j in range(V):
            if s[j]: continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via
    return d

def solution(N, road, K):
    INF = sys.maxsize
    answer=0
    graph = [[INF for cols in range(N)] for rows in range(N)]
    for r in road:
        if graph[r[0] - 1][r[1] - 1] > r[2]:
            graph[r[0] - 1][r[1] - 1] = r[2]
            graph[r[1] - 1][r[0] - 1] = r[2]

    for d in dijkstra(1, N, graph):
        if d <= K:
            answer +=1
    return answer


'''
def search(visit, graph, s, N, nxt):
    visit[s] = K-
    for j in range(N):
        if visit[j] != 0 and visit[j][1] < sinfo[1] - graph[sinfo[0]][j]:
            visit[j] = 0
        if graph[sinfo[0]][j] != 2001 and sinfo[1]-graph[sinfo[0]][j] >= 0 and visit[j] ==0:
            nxt.append([j,sinfo[1]-graph[sinfo[0]][j]])
    if len(nxt) == 0:
        return N-visit.count(0)
    return search(visit,graph,nxt.pop(0),N,nxt)

def solution(N, road, K):
    graph = [[2001 for cols in range(N)] for rows in range(N)]
    visit = [0 for i in range(N)]
    for r in road:
        if graph[r[0]-1][r[1]-1] > r[2]:
            graph[r[0]-1][r[1]-1] = r[2]
            graph[r[1]-1][r[0]-1] = r[2]

    nxt=[]
    return search(visit,graph,0,N,nxt)
'''


#print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))