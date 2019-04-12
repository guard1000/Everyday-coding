dir={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]} #0-n 1-e 2-s 3-w
def clean(board,pos,answer):
    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = 2  # 1. 현재 위치를 청소
        answer += 1
    cnt = 0
    while cnt < 4:
        if board[pos[0]+dir[(pos[2]+3)%4][0]][pos[1]+dir[(pos[2]+3)%4][1]] == 0:    #왼쪽이면 무빙
            pos[0], pos[1] = pos[0]+dir[(pos[2]+3)%4][0], pos[1]+dir[(pos[2]+3)%4][1]
            pos[2] = (pos[2]+3)%4
            return clean(board,pos,answer)
        else:
            pos[2] = (pos[2]+3)%4   #회전
        cnt += 1
        if cnt == 4 and pos[2] == 0 and board[pos[0]+1][pos[1]] != 1:    #back
            pos[0],cnt = pos[0]+1,0
        elif cnt == 4 and pos[2] == 1 and board[pos[0]][pos[1]-1] != 1:
            pos[1], cnt = pos[1] - 1, 0
        elif cnt == 4 and pos[2] == 2 and board[pos[0]-1][pos[1]] != 1:
            pos[0], cnt = pos[0] - 1, 0
        elif cnt == 4 and pos[2] == 3 and board[pos[0]][pos[1]+1] != 1:
            pos[1], cnt = pos[1] + 1, 0
    return answer

N,M = map(int,input().split())
pos = list(map(int,input().split()))
pos[0]+=1
pos[1]+=1
board=[[1 for m in range(M+2)]]
for n in range(N):
    board.append([1]+list(map(int,input().split()))+[1])
board.append([1 for m in range(M+2)])
answer=clean(board,pos,0)
print(answer)

'''
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''