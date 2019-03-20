def bfs(now,matirx, target,val):
    next=[]
    for no in now:
        if len(matrix[no[0]]) > 0:
            for i in matrix[no[0]]:
                next.append([i[0], i[1]+no[1]])
    for nxt in next:
        if nxt[0] == target and nxt[1] < val:
            val = nxt[1]
    for n in range(len(next)-1,-1,-1):
        if next[n][1] > val:    next.pop(n)
        elif next[n][1] == val and next[n][0] != target:    next.pop(n)
        elif next[n][0] == target:  next.pop(n)
    if len(next) == 0:  return val
    return bfs(next,matrix,target,val)


T = int(input())
for t in range(T):
    N,E = map(int,input().split())
    matrix=[[] for n in range(N)]
    for e in range(E):
        edge = list(map(int,input().split()))
        matrix[edge[0]].append([edge[1],edge[2]])
    print('#',end='')
    print(t+1,end=' ')
    print(bfs([[0,0]],matrix, N,999999999))


'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''