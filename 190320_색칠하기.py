T = int(input())
for t in range(T):
    N,E,M = map(int, input().split())
    matrix = [[] for n in range(N)]
    color=[0 for n in range(N)]
    color[0] = 1
    for e in range(E):
        edge = list(map(int, input().split()))
        matrix[edge[0]-1].append(edge[1]-1)
        matrix[edge[1] - 1].append(edge[0] - 1)
    for n in range(N):
        matrix[n]=sorted(matrix[n])
    print(matrix)


    for v in range(len(matrix)):
        if color[v] == 0:   #미정
            col = 1
            while col >= 1:
                chk = 0
                while chk < len(matrix[v]):
                    if color[matrix[v][chk]] == col:
                        break
                    chk += 1
                if chk != len(matrix[v]):   #걸렸음
                    col += 1
                else:
                    color[v] = col
                    break
    color = set(color)
    print('#',end='')
    print(t+1, end=' ')
    if len(color) <= M: print(1)
    else:   print(0)
'''
1
4 5 2
1 2
1 3
2 4
3 4
2 3
'''