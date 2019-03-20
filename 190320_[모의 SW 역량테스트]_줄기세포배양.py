T = int(input())
for t in range(T):
    N,M,K = map(int,input().split())
    inp,visit,die=[],[],0
    for n in range(N):
        tmp=list(map(int,input().split()))
        for t in range(len(tmp)):
            if tmp[t] != 0:
                inp.append([n,t,tmp[t],-tmp[t],0])  #[행,열,X,-X가 되면 죽음,뉴비인지마크]
                visit.append([n,t])
    for k in range(K):
        newbi=[]
        for i in inp:   #확장
            if i[2]==0:    #활성되자마자
                if [i[0] + 1, i[1]] not in visit:
                    visit.append([i[0] + 1, i[1]])
                    inp.append([i[0]+1, i[1],-i[3],i[3],1])
                if [i[0] - 1, i[1]] not in visit:
                    visit.append([i[0] - 1, i[1]])
                    inp.append([i[0]-1,i[1],-i[3],i[3],1])
                if [i[0] , i[1]+1] not in visit:
                    visit.append([i[0], i[1]+1])
                    inp.append([i[0],i[1]+1,-i[3],i[3],1])
                if [i[0] , i[1]-1] not in visit:
                    visit.append([i[0], i[1]-1])
                    inp.append([i[0],i[1]-1,-i[3],i[3],1])
        for i in range(len(inp)):  #시간댕기기
            if inp[i][4] == 1:  inp[i][4] = 0
            else:
                inp[i][2] -= 1
                if inp[i][2] == inp[i][3]:  die += 1
    print(len(inp)-die)
'''
T = int(input())
for t in range(T):
    N,M,K = map(int,input().split())
    inp,visit,die=[],[],0
    for n in range(N):
        tmp=list(map(int,input().split()))
        for t in range(len(tmp)):
            if tmp[t] != 0:
                inp.append([n,t,tmp[t],-tmp[t],0])  #[행,열,X,-X가 되면 죽음,뉴비인지마크]
                visit.append([n,t])
    for k in range(K):
        newbi=[]
        for i in inp:   #확장
            if i[2]==0:    #활성되자마자
                if [i[0] + 1, i[1]] not in visit:
                    n = 0
                    while n < len(newbi):
                        if newbi[n][:2] == [i[0] + 1, i[1]] and newbi[n][2] <= -i[3]:
                            newbi[n] = [i[0] + 1, i[1], -i[3], i[3], 1]
                            break
                        n += 1
                    if n == len(newbi):
                        newbi.append([i[0] + 1, i[1], -i[3], i[3], 1])

                if [i[0] - 1, i[1]] not in visit:
                    n = 0
                    while n < len(newbi):
                        if newbi[n][:2] == [i[0] - 1, i[1]] and newbi[n][2] <= -i[3]:
                            newbi[n] = [i[0] - 1, i[1], -i[3], i[3], 1]
                            break
                        n += 1
                    if n == len(newbi):
                        newbi.append([i[0] - 1, i[1], -i[3], i[3], 1])

                if [i[0] , i[1]+1] not in visit:
                    n = 0
                    while n < len(newbi):
                        if newbi[n][:2] == [i[0], i[1]+1] and newbi[n][2] <= -i[3]:
                            newbi[n] = [i[0], i[1]+1, -i[3], i[3], 1]
                            break
                        n += 1
                    if n == len(newbi):
                        newbi.append([i[0], i[1]+1, -i[3], i[3], 1])

                if [i[0] , i[1]-1] not in visit:
                    n=0
                    while n < len(newbi):
                        if newbi[n][:2] == [i[0], i[1]-1] and newbi[n][2] <= -i[3]:
                            newbi[n] = [i[0], i[1]-1, -i[3], i[3], 1]
                            break
                        n += 1
                    if n == len(newbi):
                        newbi.append([i[0], i[1]-1, -i[3], i[3], 1])
        for newb in newbi:
            visit.append([newb[0],newb[1]])
            inp.append(newb)

        for i in range(len(inp)):  #시간댕기기
            if inp[i][4] == 1:  inp[i][4] = 0
            else:
                inp[i][2] -= 1
                if inp[i][2] == inp[i][3]:  die += 1
    print(len(inp)-die)
'''





'''
1
2 2 10
1 1
0 2
'''