T = int(input())
for t in range(T):
    N = int(input())
    matrix =[]
    for n in range(N):
        matrix.append(list(map(int,input().split())))
    board=[[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j != 0:
                tmp=0
                if matrix[i][j] > matrix[i][j-1]:
                    tmp = matrix[i][j]-matrix[i][j-1]
                board[i][j] = tmp +board[i][j-1]+1
            elif j == 0 and i != 0:
                tmp =0
                if matrix[i][j] > matrix[i-1][j]:
                    tmp = matrix[i][j]-matrix[i-1][j]
                board[i][j] = tmp +board[i-1][j]+1
            elif j !=0 and i != 0:
                tmp1,tmp2=0,0
                if matrix[i][j] > matrix[i][j-1]:
                    tmp1 = matrix[i][j]-matrix[i][j-1]
                if matrix[i][j] > matrix[i - 1][j]:
                    tmp2 = matrix[i][j]-matrix[i-1][j]
                board[i][j] = min(tmp1 +board[i][j-1]+1, tmp2 +board[i-1][j]+1)
    print('#',end='')
    print(t+1,end=' ')
    print(board[N-1][N-1])



'''
1
3
0 2 1
0 1 1
1 1 1
'''

'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''