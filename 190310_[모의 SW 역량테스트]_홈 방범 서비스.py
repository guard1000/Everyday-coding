dir=[[-1,0],[1,0],[0,-1],[0,1]]

def able(now,visits,K,N,homes,cnt):
    global dir
    next=[]
    for visit in now:
        for d in dir:
            nxt = [visit[0]+d[0],visit[1]+d[1]]
            if nxt not in visits and (0 <= nxt[0] < N) and (0 <= nxt[1] < N) and nxt in homes:
                cnt += 1
                next.append(nxt)
                visits.append(nxt)
            elif nxt not in visits and (0 <= nxt[0] < N) and (0 <= nxt[1] < N):
                visits.append(nxt)
                next.append(nxt)
    K -= 1
    if K == 1:  return cnt
    return able(next,visits,K,N,homes,cnt)

answer=0
T = int(input())
for t in range(T):
    answer=0
    N,M = map(int, input().split())
    homes=[]
    for n in range(N):
        board=list(map(int, input().split()))
        for j in range(len(board)):
            if board[j] == 1: homes.append([n,j])

    K = 2
    while K <= N*2 and K * K + (K - 1) * (K - 1) <= len(homes) * M:
        print(K)
        for i in range(N):
            for j in range(N):
                if [i,j] in homes:
                    tmp = able([[i,j]], [[i,j]], K, N, homes, 1)
                    if tmp*M >= K*K+(K-1)*(K-1) and tmp > answer:
                        answer = tmp
                else:
                    tmp = able([[i, j]], [[i, j]], K, N, homes, 0)
                    if tmp*M >= K*K+(K-1)*(K-1) and tmp > answer:
                        answer = tmp
    
        K += 1
    print('#',end='')
    print(t+1,end=' ')
    print(answer)


'''
def able(homes,x,y,K,M):
    n=0
    for home in homes:
        if (x-home[0])**2+(y-home[1])**2 <= (K-1)**2:
            n += 1
    if n*M >= K*K+(K-1)*(K-1):
        return n
    return -1

T = int(input())
for t in range(T):
    answer=0
    N,M = map(int, input().split())
    homes=[]
    for n in range(N):
        board=list(map(int, input().split()))
        for j in range(len(board)):
            if board[j] == 1: homes.append([n,j])
    K=1
    while K*K+(K-1)*(K-1) <= len(homes)*M:
        for i in range(N):
            for j in range(N):
                if able(homes,i,j,K,M) > answer:
                    print(answer, i, j, K)
                    answer = able(homes,i,j,K,M)
        K += 1
    print(homes)
    print(answer)
'''

'''
def able(board,row,col,K):
    num=0
    r,c = row-(K-1),col-(K-1)
    for i in range(r,r+2*K-1,1):
        for j in range(c,c+2*K-1,1):
            if (i >= 0 and i <len(board)) and (j >= 0 and j <len(board)):
                if board[i][j] == 1 and ((row-i)**2 + (col-j)**2) <= (K-1)**2:
                    num += 1
    return num

def value(board,row,col,K,M):
    cost, n = K*K+(K-1)*(K-1), able(board,row,col,K)
    if M*n-cost >= 0:
        return n
    return 0

T = int(input())
for t in range(T):
    answer,cnt = 0,0
    N,M = map(int, input().split())
    board=[]
    for n in range(N):
        board.append(list(map(int, input().split())))
        cnt += board[-1].count(1)
    for K in range(1,N):
        if K*K+(K-1)*(K-1) > cnt*M:
            break
        for i in range(N):
            for j in range(N):
                if value(board,i,j,K,M) > answer:
                    answer = value(board,i,j,K,M)

    print(able(board,5,8,11))
    print(((14-5)**2 + (4-8)**2))
'''