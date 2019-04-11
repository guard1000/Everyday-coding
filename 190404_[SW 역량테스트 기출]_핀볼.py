import copy
import sys
sys.setrecursionlimit(10**9)
def playgame(i,j,d,gameboard,score,pair,endpoint):    #d0-up d1-down d2-left d3-left
    if gameboard[i][j] == -1 or [i,j]==endpoint:   return score
    if gameboard[i][j] == 1:    #directrion control
        if d == 0:  d = 1
        elif d == 1:    d = 3
        elif d == 2:    d = 0
        elif d == 3:    d = 2
        score += 1
    elif gameboard[i][j] == 2:
        if d == 0:  d = 3
        elif d == 1:    d = 0
        elif d == 2:    d = 1
        elif d == 3:    d = 2
        score += 1
    elif gameboard[i][j] == 3:
        if d == 0:  d = 2
        elif d == 1:    d = 0
        elif d == 2:    d = 3
        elif d == 3:    d = 1
        score += 1
    elif gameboard[i][j] == 4:
        if d == 0:  d = 1
        elif d == 1:    d = 2
        elif d == 2:    d = 3
        elif d == 3:    d = 0
        score += 1
    elif gameboard[i][j] == 5:
        if d == 0:  d = 1
        elif d == 1:    d = 0
        elif d == 2:    d = 3
        elif d == 3:    d = 2
        score += 1

    elif gameboard[i][j] > 5:  #move control
        return playgame(pair[gameboard[i][j]-6][0]-i,pair[gameboard[i][j]-6][1]-j,d,gameboard,score,pair,endpoint)

    if d == 0:  return playgame(i-1,j,d,gameboard,score,pair,endpoint)
    elif d == 1:    return playgame(i+1,j,d,gameboard,score,pair,endpoint)
    elif d == 2:    return playgame(i,j-1,d,gameboard,score,pair,endpoint)
    else:   return playgame(i, j+1, d, gameboard, score, pair,endpoint)

T = int(input())
for t in range(T):
    answer = 0
    N = int(input())    #input
    pair = [[0,0],[0,0],[0,0],[0,0],[0,0]]  #6,7,8,9,10
    board=[[5 for i in range(N+2)]]
    for n in range(N):
        board.append([5]+list(map(int,input().split()))+[5])
    board.append([5 for i in range(N+2)])

    for b in range(N+2):
        print(board[b])

    for i in range(1, N):   #wormhole pair-sum check
        for j in range(1,N):
            if board[i][j] > 5:
                pair[board[i][j] - 6][0] += i
                pair[board[i][j] - 6][1] += j

    for i in range(1, N + 2):   #start
        for j in range(1,N+2):
            if board[i][j] == 0:
                endpoint=[i,j]
                for d in range(4):  #direction 0,1,2,3
                    gameboard = copy.deepcopy(board)
                    if d == 0:
                        tmp = playgame(i - 1, j, d, gameboard, 0, pair, endpoint)
                    elif d == 1:
                        tmp = playgame(i + 1, j, d, gameboard, 0, pair, endpoint)
                    elif d == 2:
                        tmp = playgame(i, j - 1, d, gameboard, 0, pair, endpoint)
                    else:
                        tmp = playgame(i, j + 1, d, gameboard, 0, pair, endpoint)
                    if tmp > answer:  answer = tmp
                    print(answer)


    for b in range(N+2):
        print(board[b])
    print(pair)
    print(answer)

'''
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
'''