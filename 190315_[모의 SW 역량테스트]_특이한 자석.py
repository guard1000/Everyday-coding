def spinning(wheels, spin, visit):
    nxt=[]
    for s in spin:
        visit.append(s[0])
        if 0 < s[0] < 3:    #얘로 인해 돌아가게 되는 녀석들을 nxt에 넣어줌
            if wheels[s[0]][2] != wheels[s[0]+1][-2] and s[0]+1 not in visit and s[0]+1 not in nxt:   #오른쪽
                nxt.append([s[0]+1,0-s[1]])
            if wheels[s[0]][-2] != wheels[s[0]-1][2] and s[0]-1 not in visit and s[0]-1 not in nxt:   #왼쪽
                nxt.append([s[0]-1,0-s[1]])
        elif s[0] == 0:
            if wheels[s[0]][2] != wheels[s[0]+1][-2] and s[0]+1 not in visit and s[0]+1 not in nxt:   #오른쪽
                nxt.append([s[0]+1,0-s[1]])
        else:
            if wheels[s[0]][-2] != wheels[s[0]-1][2] and s[0]-1 not in visit and s[0]-1 not in nxt:   #왼쪽
                nxt.append([s[0]-1,0-s[1]])
        if s[1] == -1:   #반시계 회전
            wheels[s[0]] = wheels[s[0]][1:]+[wheels[s[0]][0]]
        elif s[1] == 1: #시계 회전
            wheels[s[0]] = [wheels[s[0]][-1]]+wheels[s[0]][:-1]
    if len(nxt) == 0:   return wheels
    return spinning(wheels,nxt,visit)


T = int(input())
for t in range(T):
    answer=0
    K = int(input())    #입력
    wheels, spins =[],[]
    for i in range(4):
        wheels.append(list(map(int, input().split())))
    for k in range(K):  #회전시킬 톱니와 방향 입력
        spins.append(list(map(int,input().split())))
        spins[-1][0] -= 1
    for spin in spins:
        wheels = spinning(wheels, [spin], [])
    for i in range(4):
        answer += wheels[i][0]*(2**i)
    print('#',end='')
    print(t+1,end=' ')
    print(answer)


'''
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
'''