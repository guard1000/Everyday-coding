import copy
import itertools
def infection(lab,now):
    nxt=[]
    for no in now:
        if no[0]>0 and lab[no[0]-1][no[1]] == 0 and [no[0]-1,no[1]] not in nxt:    #up
            nxt.append([no[0]-1,no[1]])
        if no[0]<len(lab)-1 and lab[no[0]+1][no[1]] == 0 and [no[0]+1,no[1]] not in nxt:    #down
            nxt.append([no[0] + 1, no[1]])
        if no[1] > 0 and lab[no[0]][no[1]-1] == 0 and [no[0], no[1]-1] not in nxt:  # left
            nxt.append([no[0], no[1]-1])
        if no[1]<len(lab[0])-1 and lab[no[0]][no[1]+1] == 0 and [no[0],no[1]+1] not in nxt:    #right
            nxt.append([no[0], no[1]+1])
    if len(nxt) == 0:
        val = 0
        for i in range(len(lab)):
            val += lab[i].count(0)
        return val
    for nx in nxt:
        lab[nx[0]][nx[1]] = 2
    return infection(lab,nxt)

N,M = map(int,input().split())
lab,candi,virus,answer = [],[],[],0
for n in range(N):
    lab.append(list(map(int,input().split())))
    for j in range(M):
        if lab[-1][j] == 0: candi.append([n,j])
        elif lab[-1][j] == 2: virus.append([n,j])

mycombination = itertools.combinations(candi,3)
for mycomb in mycombination:
    newlab = copy.deepcopy(lab)
    newvirus = copy.deepcopy(virus)
    for comb in mycomb:
        newlab[comb[0]][comb[1]] = 1
    tmp = infection(newlab,newvirus)
    if tmp > answer:
        answer = tmp

print(answer)



'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''