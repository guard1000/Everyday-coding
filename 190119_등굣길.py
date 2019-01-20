def solution(m, n, puddles):
    answer = 0
    #table 만들기 puddle은 -1로 초기화
    table=[[0 for i in range(m+1)]for j in range(n+1)]
    table[1][1] = 1
    for puddle in puddles:
        table[puddle[1]][puddle[0]] = -1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if table[i][j] != -1 and table[i][j-1] != -1:
                table[i][j] += table[i][j-1]
            if table[i][j] != -1 and table[i-1][j] != -1:
                table[i][j] += table[i-1][j]

    print(table)
    return table[n][m]%1000000007



'''
def go(now,table,flag,m,n):
    if flag == 0:
        return table[n][m]
    nxt=[]
    for i in now:
        if i[1]< m and table[i[0]][i[1]+1] != -1:
            table[i[0]][i[1] + 1] += table[i[0]][i[1]]
            if [i[0],i[1]+1] not in nxt:
                nxt.append([i[0],i[1]+1])
            if i[0] == n and i[1]+1 == m:
                flag -= 1
        if i[0]< n and table[i[0]+1][i[1]] != -1:
            table[i[0]+1][i[1]] += table[i[0]][i[1]]
            if [i[0]+1, i[1]] not in nxt:
                nxt.append([i[0]+1, i[1]])
            if i[0]+1 == n and i[1] == m:
                flag -= 1
    return go(nxt,table,flag,m,n)


def solution(m, n, puddles):
    answer = 0
    #table 만들기 puddle은 -1로 초기화
    table=[[0 for i in range(m)]for j in range(n)]
    table[0][0] = 1
    for puddle in puddles:
        table[puddle[1]-1][puddle[0]-1] = -1

    #flag 초기화: 도착점의 위, 왼쪽에 웅덩이가 있을 경우를 따짐
    flag = 2
    if [m,n-1]in puddles or [m-1,n] in puddles :
        flag -= 1
    return go([[0,0]],table,flag,m-1,n-1)%1000000007
'''


print(solution(4,3,[[2,2]]))
print(solution(6,4,[[1,3],[3,2],[5,4],[5,3]]))