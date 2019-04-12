N,M,x,y,K = map(int, input().split())
number = 0
dice =[[0 ,0, 0],
       [0, 0, 0],
       [0, 0, 0]]
board=[]
for n in range(N):
    board.append(list(map(int,input().split())))
move = list(map(int,input().split()))

for k in range(K):
    if move[k] == 1 and y < M-1:    #동쪽
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = number
        if board[x][y+1] == 0:  board[x][y+1],number=tmp,tmp
        else:
            number = board[x][y+1]
            board[x][y + 1] = 0
        x,y=x,y+1
        print(dice[1][1])
    elif move[k] == 2 and y > 0:    #서쪽
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = number
        if board[x][y-1] == 0:  board[x][y-1],number=tmp,tmp
        else:
            number = board[x][y-1]
            board[x][y - 1] = 0
        x,y=x,y-1
        print(dice[1][1])
    elif move[k] == 3 and x > 0:    #북쪽
        tmp = dice[0][1]
        dice[0][0] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = number
        if board[x-1][y] == 0:  board[x-1][y],number=tmp,tmp
        else:
            number = board[x-1][y]
            board[x-1][y] = 0
        x,y=x-1,y
        print(dice[1][1])
    elif move[k] == 4 and x < N-1:    #남쪽
        tmp = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = number
        if board[x+1][y] == 0:  board[x+1][y],number=tmp,tmp
        else:
            number = board[x+1][y]
            board[x+1][y] = 0
        x,y=x+1,y
        print(dice[1][1])

    for d in range(len(dice)):
        print(dice[d], board[d])
    print(number)
    print()



'''
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
'''