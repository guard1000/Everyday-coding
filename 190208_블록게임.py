def black(board,n):
    for i in range(n):
        if board[0][i] == 0:
            board[0][i] = -1
    for i in range(1,n):
        for j in range(n):
            if board[i][j] <= 0 and board[i-1][j] == -1:
                board[i][j] = -1
    return board

def erase(board,n,cnt):
    cnt2=0
    for i in range(n-2):    #3*2
        for j in range(n-1):
            count={}    #-1갯수,색의 수
            for y in range(3):
                for x in range(2):
                    if board[i+y][x+j] in count:
                        count[board[i+y][x+j]] += 1
                    else:
                        count[board[i + y][x + j]] = 1
            if -1 in count and len(count) == 2 and count[-1] ==2 and 0 not in count:   #erasable
                cnt2 += 1
                for y in range(3):
                    for x in range(2):
                        board[i+y][j+x] = 0
                board = black(board,n)

    for i in range(n - 1):  # 2*3
        for j in range(n - 2):
            count = {}  # -1갯수,색의 수
            for y in range(2):
                for x in range(3):
                    if board[i + y][x + j] in count:
                        count[board[i + y][x + j]] += 1
                    else:
                        count[board[i + y][x + j]] = 1
            if -1 in count and len(count) == 2 and count[-1] == 2 and 0 not in count:  # erasable
                cnt2 += 1
                for y in range(2):
                    for x in range(3):
                        board[i+y][j+x] = 0
                board = black(board,n)

    if cnt2 == 0:
        return cnt
    return erase(board,n,cnt+cnt2)

def solution(board):
    n = len(board)
    board = black(board,n)
    return erase(board,n,0)

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))