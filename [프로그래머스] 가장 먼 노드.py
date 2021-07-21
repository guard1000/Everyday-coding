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