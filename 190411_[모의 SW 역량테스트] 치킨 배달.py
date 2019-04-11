import itertools
import copy

def nearkfc(visit, now, val,city):
    nxt=[]
    for no in now:
        if 0 < no[0] and [no[0]-1,no[1]] not in visit and [no[0]-1,no[1]] not in nxt: nxt.append([no[0]-1,no[1]])#up
        if no[0] < len(city)-1 and [no[0] + 1, no[1]] not in visit and [no[0] + 1, no[1]] not in nxt: nxt.append([no[0] + 1, no[1]])  #down
        if 0 < no[1] and [no[0] , no[1]-1] not in visit and [no[0] , no[1]-1] not in nxt: nxt.append([no[0] , no[1]-1])  #left
        if no[1] < len(city)-1 and [no[0], no[1]+1] not in visit and [no[0], no[1]+1] not in visit : nxt.append([no[0], no[1]+1])  #right
    val += 1
    for n in nxt:
        if city[n[0]][n[1]] == 3:   return val
    visit = visit+nxt
    return nearkfc(visit, nxt, val, city)

def kfc_distance(target, kfc, home, city):
    distance = 0
    for t in target:
        city[kfc[t][0]][kfc[t][1]] = 3
    for h in home:
        distance += nearkfc([h],[h],0,city)
    return distance

N, M = map(int, input().split())
city=[]
home=[]
kfc=[]
answer = 1000
for n in range(N):  #input
    city.append(list(map(int,input().split())))
    for m in range(N):
        if city[-1][m] == 1:    home.append([n,m])
        elif city[-1][m] == 2:  kfc.append([n,m])

target=[i for i in range(len(kfc))]
mycombination = itertools.combinations(target,M)
for mycomb in mycombination:
    newcity = copy.deepcopy(city)
    tmp = kfc_distance(mycomb,kfc,home,newcity)
    if tmp < answer:    answer = tmp

print(answer)

'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''