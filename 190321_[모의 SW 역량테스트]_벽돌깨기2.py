import itertools
import copy
def bomb(board2, pos):
    nxt=[]
    if len(pos) == 0:   return board2
    cnt = 0
    for row in board2:
        cnt += sum(row)
    if cnt == 0:    return board2
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
            board2[p[0]][p[1]-c] = 0
        for c in range(1,d):  #right
            if p[1] + c >= len(board2[0]): break
            elif board2[p[0]][p[1]+c] != 1 and [p[0],p[1]+c,board2[p[0]][p[1]+c]] not in nxt: nxt.append([p[0],p[1]+c,board2[p[0]][p[1]+c]])
            board2[p[0]][p[1]+c] = 0
    return bomb(board2,nxt)

def drop(board3):
    for col in range(len(board3[0])):
        p = len(board3)-1
        for row in range(len(board3)-1,-1,-1):
            if board3[row][col] != 0:
                temp = board3[row][col]
                board3[row][col] = 0
                board3[p][col] = temp
                p -= 1
    return board3

T = int(input())
for t in range(T):
    N,W,H = map(int,input().split())
    minimum = W * H
    matrix = []
    for h in range(H):
        matrix.append(list(map(int,input().split())))
    #열 조합 만들기 - target[] 에 들어있음
    target,num=[],[i for i in range(W)]
    targets = itertools.product(num, repeat=N)
    for tar in targets:
        target.append(list(tar))

    for tar in target:  #target에 있는거 하나씩 해봐 ㅎㅎ
        tmp = copy.deepcopy(matrix) #tmp에 matrix 복제해서 시물레이션
        for col in tar:
            row = 0
            while row < len(tmp):
                if tmp[row][col] != 0:
                    break
                row += 1
            if row == len(tmp): #끝까지 0이면 이 케이스는 오버트
                break
            tmp = bomb(tmp,[[row,col,tmp[row][col]]])
            tmp = drop(tmp)

            zero=0
            for t2 in tmp:
                zero += t2.count(0)
            result = W*H-zero
            if result < minimum:
                minimum = result
            if minimum == 0:    break
        if minimum == 0:    break

    print('#', end='')
    print(t+1, end=' ')
    print(minimum)



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