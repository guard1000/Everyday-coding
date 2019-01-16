answer=[]
INF = 1001

def dijkstra(start, N, graph, end):
    '''
    dist = [INF for x in range(N)]
    visit = [0 for x in range(N)]

    dist[start] = 0
    for i in range(1,N+1):
        min = INF
        for j in range(1, N+1):
            if visit[j] == 0 and min > dist[j]:
                min = dist[j]
                v = j
        visit[v] = 1
        for j in range(1, N+1):
            if dist[j] > dist[v] + graph[v][j]:
                dist[j] = dist[v] + graph[v][j]
    return dist[end]
'''
    s = [False] * N
    d = [INF] * N
    d[start-1] = 0
    while True:
        m = INF
        N2 = -1
        for j in range(N):
            if not s[j] and m > d[j]:
                m = d[j]
                N2 = j
        if m == INF:
            break
        s[N2] = True

        for j in range(N):
            if s[j]: continue
            via = d[N2] + graph[N2][j]
            if d[j] > via:
                d[j] = via
    return d[end-1]


#메인
n = int(input())    # 테스트케이스 몇개인지 입력받음
for i in range(n):
    N, M, K, S = map(int, input().split()) # N M K S 입력
    k = list(map(int, input().split())) #돌아야 할 경로 입력
    k = [S] + k + [S]   # 시작과 끝은 S에서 시작해서 S에서 끝
    graph=[[INF for rows in range(N)]for cols in range(N)]
    for j in range(N):
        graph[j][j] = 0

    for j in range(M):      #맵그리기
        u, v= map(int, input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1

    for l in range(len(k)-1):
        answer.append(dijkstra(k[l], N,graph, k[l+1]))


for i in range(n):
    print('#', end='')
    print(i+1, answer[i])