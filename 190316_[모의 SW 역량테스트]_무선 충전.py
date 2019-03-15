dir={0:[0,0],1:[-1,0],2:[0,1],3:[1,0],4:[0,-1]}
def move(pos, d):
    return [pos[0]+dir[d][0],pos[1]+dir[d][1]]

def charge(posA,posB,AP):
    charging=0
    ableA,ableB=[],[]
    for i in range(len(AP)):
        if abs(AP[i][0]-posA[0])+abs(AP[i][1]-posA[1]) <= AP[i][2]: #A가 충전범위 안에 있으면
            ableA.append(i)
        if abs(AP[i][0]-posB[0])+abs(AP[i][1]-posB[1]) <= AP[i][2]: #B가 충전범위 안에 있으면
            ableB.append(i)
    for i in ableA:
        for j in ableB:
            if i==j:    tmp=AP[i][3]
            else:   tmp=AP[i][3]+AP[j][3]
            if tmp > charging:  charging = tmp
    if len(ableB)==0:
        for i in ableA:
            if AP[i][3] > charging: charging=AP[i][3]
    elif len(ableA)==0:
        for i in ableB:
            if AP[i][3] > charging: charging=AP[i][3]
    return charging

T = int(input())
for t in range(T):
    answer = 0
    M,A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    posA, posB= [0,0],[9,9]
    AP=[]
    for a in range(A):
        AP.append(list(map(int,input().split())))
        AP[-1][0],AP[-1][1]=AP[-1][1]-1,AP[-1][0]-1 #아 이거 바뿨줘야되네
    for i in range(M):
        answer += charge(posA,posB,AP)
        posA= move(posA,A_move[i])  #이동
        posB= move(posB,B_move[i])
    answer += charge(posA, posB, AP)

    print('#',end='')
    print(t+1,end=' ')
    print(answer)


'''
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
'''