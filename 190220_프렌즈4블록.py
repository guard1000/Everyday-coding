def clear_drop(m,n,board):
    cnt=0
    for i in range(m-2,-1,-1):  #삭제할 것 삭제
        for j in range(n-2,-1,-1):
            if board[i][j][1] == -1 and board[i][j][0] != -1:    #삭제 대상
                cnt += 1
                board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1] = [-1,-1],[-1,-1],[-1,-1],[-1,-1]
    if cnt == 0:#더이상 삭제할 것이 없음 -> 끝
        answer=0
        for i in range(m):
            for j in range(n):
                if board[i][j] == [-1,-1]:
                    answer += 1
        return answer
    for i in range(m-1, 0, -1): #drop
        for j in range(n):
            if board[i][j] == [-1,-1]:
                x,y=i-1,j
                while x>=0 and board[x][y] == [-1,-1]:
                    x -= 1
                if x != -1:
                    board[i][j] = board[x][y]
                    board[x][y] = [-1,-1]
    return board

def check(x,y,board):
    if board[x][y][0] != -1 and board[x+1][y][0] == board[x][y][0] and board[x][y+1][0] == board[x][y][0] and board[x+1][y+1][0] == board[x][y][0]:
        return True
    return False

def solution(m, n, board):
    for i in range(m):  #board 형 변환
        board[i] = list(board[i])
        for j in range(n):
            board[i][j] = [board[i][j],0]
    while type(board) != int:
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if check(i,j,board):
                    board[i][j][1] = -1
        board = clear_drop(m,n,board)
    return board


print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
