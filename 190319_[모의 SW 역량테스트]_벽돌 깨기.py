import itertools
def bomb(board2, pos):
    nxt=[]
    if len(pos) == 0:   return board2
    for p in pos:   #다음 폭발
        d = p[2]
        board2[p[0]][p[1]] = 0   #펑
        for r in range(1,d):  #up
            if p[0] - r < 0 or board2[p[0] - r][p[1]] == 0: break
            elif board2[p[0]-r][p[1]] != 1 and [p[0]-r,p[1],board2[p[0]-r][p[1]]] not in nxt: nxt.append([p[0]-r,p[1],board2[p[0]-r][p[1]]])
            board2[p[0] - r][p[1]] = 0
        for r in range(1,d):  #down
            if p[0] + r >= len(board2) or board2[p[0] + r][p[1]] == 0: break
            elif board2[p[0]+r][p[1]] != 1 and [p[0]+r,p[1],board2[p[0]+r][p[1]]] not in nxt: nxt.append([p[0]+r,p[1],board2[p[0]+r][p[1]]])
            board2[p[0] + r][p[1]] = 0
        for c in range(1,d):  #left
            if p[1] - c < 0:  break
            elif board2[p[0]][p[1]-c] != 1 and [p[0],p[1]-c,board2[p[0]][p[1]-c]] not in nxt: nxt.append([p[0],p[1]-c,board2[p[0]][p[1]-c]])
            board[p[0]][p[1]-c] = 0
        for c in range(1,d):  #right
            if p[1] + c >= len(board2[0]): break
            elif board2[p[0]][p[1]+c] != 1 and [p[0],p[1]+c,board2[p[0]][p[1]+c]] not in nxt: nxt.append([p[0],p[1]+c,board2[p[0]][p[1]+c]])
            board2[p[0]][p[1]+c] = 0
    return bomb(board2,nxt)

def drop(board):
    for col in range(len(board[0])):
        p = len(board)-1
        for row in range(len(board)-1,-1,-1):
            if board[row][col] != 0:
                temp = board[row][col]
                board[row][col] = 0
                board[p][col] = temp
                p -= 1
    return board

def cnt(board):
    zero_sum=0
    for b in board:
        zero_sum += b.count(0)
    return len(board)*len(board[0])-zero_sum

T = int(input())
for t in range(T):
    N,W,H = map(int, input().split())
    answer=N*H
    board=[]
    for h in range(H):
        board.append(list(map(int,input().split())))
    target = [i for i in range(W)]
    mypermutation = itertools.product(target, repeat=N)
    for permutation in mypermutation:
        tmp = board[:]
        print(tmp)
        for col in permutation:
            if tmp[H-1][col] == 0:
                break
            for row in range(H):
                if tmp[row][col] != 0:
                    break
            print([row,col])
            tmp = bomb(tmp,[[row,col,tmp[row][col]]])
            print('bb',board)
            tmp = drop(tmp)
        if cnt(tmp) < answer:
            answer = cnt(tmp)

            print(permutation, answer)
        print('b',board)

    print(answer)





'''
    for n in range(N):
        target=[0,0]
        for col in range(W):
            flag = 0
            for row in range(H):
                if row == H-1 and board[row][col]==0:
                    flag = 1
                if board[row][col] != 0:
                    break
            if flag == 1:
                flag = 0
                break
            tmp = bomb(board,[[row,col,board[row][col]]])
            if answer > cnt(tmp):
                answer = cnt(tmp)
                target = [row,col]
        board = bomb(board,[[target[0],target[1],board[target[0]][target[1]]]])
        board = drop(board)
        answer = cnt(board)
        print(answer, target)
    print(answer)
'''


'''
    tmp = bomb(board,[[2,2,board[2][2]]])
    for t in tmp:
        print(t)

    print('222')

    tmp = drop(board)
    for t in tmp:
        print(t)

    print(cnt(tmp))
'''

'''
    for n in range(N):
        for i in range(W - 1, -1, -1):  # 구슬 비었을 경우
            if board[H - 1][i] == 0 and i in target:  target.remove(i)
'''




'''
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''