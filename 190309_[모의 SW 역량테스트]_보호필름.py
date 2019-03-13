import itertools

def check(board,K):
    for col in range(len(board[0])):
        cnt=0
        for row in range(1,len(board)):
            if board[row][col] == board[row-1][col]:
                cnt += 1
                if cnt >= K-1:
                    break
            else:
                cnt = 0
        if cnt<K-1:
            return False
    return True


T = int(input())
for t in range(T):
    D,W,K = map(int, input().split())
    board=[]
    for d in range(D):
        board.append(list(map(int, input().split())))
    if check(board,K):
        print('#',end='')
        print(t+1, end=' ')
        print(0)
    else:
        candi=[i for i in range(D)]
        for k in range(1,K+1):
            flag=0
            mycombination = itertools.combinations(candi,k)
            for mycomb in mycombination:
                test=board[:]
                for comb in mycomb:
                    test[comb]=[0 for j in range(W)]
                if check(test,K):
                    print('#', end='')
                    print(t + 1, end=' ')
                    print(k)
                    flag=1
                    break
                else:
                    for comb in mycomb:
                        test[comb] = [1 for j in range(W)]
                    if check(test, K):
                        print('#', end='')
                        print(t + 1, end=' ')
                        print(k)
                        flag=1
                        break
            if flag == 1:   break





