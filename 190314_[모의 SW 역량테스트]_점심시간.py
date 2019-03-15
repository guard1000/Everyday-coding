import itertools

def total_time(order, people, stair, time):
    A,B=[],[]
    A_stair,B_stair=[],[]
    for o in range(len(order)):
        if order[o] == 1:
            A.append(people[o])
        else:
            B.append(people[o])
    A = sorted(A,key=lambda x: x[0])
    B = sorted(B,key=lambda x: x[1])
    atime,btime=0,0
    for a in A:
        for As in A_stair:  #time 지났으면 빼줘
            if As+stair[0] <= atime:  A_stair.remove(As)
        if len(A_stair) < 3:    #계단 아직 자리있으면 들가
            if a[0]+1 <= atime:
                A_stair.append(atime)
            else:
                A_stair.append(a[0]+1)
                atime=A_stair[-1]
        else:
            atime=A_stair[0]+stair[0]
            A_stair.pop(0)
            if atime > a[0]:
                A_stair.append(atime)
            else:
                A_stair.append(atime+1)
                atime+=1
        if atime+stair[0] > time:    return time+1

    for b in B:
        for Bs in B_stair:  #time 지났으면 빼줘
            if Bs+stair[1] <= btime:  B_stair.remove(Bs)
        if len(B_stair) < 3:    #계단 아직 자리있으면 들가
            if b[1]+1 <= btime:
                B_stair.append(btime)
            else:
                B_stair.append(b[1]+1)
                btime=B_stair[-1]
        else:
            btime=B_stair[0]+stair[1]
            B_stair.pop(0)
            if btime > b[1]:
                B_stair.append(btime)
            else:
                B_stair.append(btime+1)
                btime+=1
        if btime+stair[1] > time: return time+1

    return max(atime+stair[0],btime+stair[1])

T = int(input())
for t in range(T):
    answer=1000
    N = int(input())    #입력받기
    board=[]
    for n in range(N):
        board.append(list(map(int,input().split())))
    people,stair=[],[]
    for row in range(N):    #people, stair 위치 찾기
        for col in range(N):
            if board[row][col] == 1:
                people.append([row,col])
            elif board[row][col] >= 2:
                stair.append([row,col,board[row][col]])
    for p in range(len(people)):    #people들 sair로 거리들
         people[p] = [ abs(people[p][0]-stair[0][0])+abs(people[p][1]-stair[0][1]),
                       abs(people[p][0]-stair[1][0])+abs(people[p][1]-stair[1][1]) ]
    stair=[stair[0][2],stair[1][2]]

    order = [1 for i in range(len(people))]
    num = [i for i in range(len(people))]
    for n in range(len(people)+1):
        mycombination = itertools.combinations(num,n)
        for combination in mycombination:
            tmp_order = order[:]
            for comb in combination:
                tmp_order[comb] = 2

            tmp = total_time(tmp_order,people,stair,answer)
            if answer > tmp:    answer = tmp
    print('#',end='')
    print(t+1,end=' ')
    print(answer)
'''
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0

[[0, 1], [0, 2], [1, 2], [2, 1], [2, 3], [4, 0]]
[[1, 4, 3], [4, 2, 5]]

[[7, 10], [6, 9], [5, 8], [7, 8], [5, 8], [10, 7]] - people

[[4, 5], [3, 4], [2, 3], [4, 3], [2, 3], [7, 2]] - 도착시간만

'''