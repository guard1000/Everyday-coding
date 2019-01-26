def solution(n, edge):
    visit=[0 for i in range(n)]
    visit[0]=1
    cnt=1
    graph=[[] for rows in range(n)]
    for ed in edge:
        graph[ed[0]-1].append(ed[1]-1)
        graph[ed[1]-1].append(ed[0]-1)
    nxt = graph[0]
    for i in nxt:
        cnt += 1
        visit[i] = 1
    while cnt < n:
        tmp=[]
        for i in nxt:
            for j in graph[i]:
                if visit[j] == 0:
                    visit[j] = 1
                    cnt += 1
                    tmp.append(j)
        nxt=tmp
    return len(nxt)


'''
def solution(n, edge):
    visit=[0 for i in range(n)]
    visit[0]=1
    graph=[[0 for cols in range(n)] for rows in range(n)]
    for ed in edge:
        graph[ed[0]-1][ed[1]-1] = 1
        graph[ed[1]-1][ed[0]-1] = 1
    nxt=[]
    for i in range(n):
        if graph[0][i] == 1 and visit[i] == 0:
            visit[i] = 1
            nxt.append(i)
    while sum(visit) < n:
        tmp=[]
        for i in nxt:
            for j in range(n):
                if graph[i][j] == 1 and visit[j] == 0:
                    visit[j] = 1
                    tmp.append(j)
        nxt=tmp
    return len(nxt)
'''
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
