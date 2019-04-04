import copy
def target(now, fishes,visit,cnt,N,sharkpower,matrix):
    nxt=[]
    cnt += 1
    for n in now:
        if n[0]>0 and [n[0]-1,n[1]] not in visit and sharkpower >= matrix[n[0]-1][n[1]]:
            nxt.append([n[0]-1,n[1]])
        if n[1]>0 and [n[0],n[1]-1] not in visit and sharkpower >= matrix[n[0]][n[1]-1]:
            nxt.append([n[0],n[1]-1])
        if n[0]<N-1 and [n[0]+1,n[1]] not in visit and sharkpower >= matrix[n[0]+1][n[1]]:
            nxt.append([n[0]+1,n[1]])
        if n[1]<N-1 and [n[0],n[1]+1] not in visit and sharkpower >= matrix[n[0]][n[1]+1]:
            nxt.append([n[0],n[1]+1])
    nxt = sorted(nxt, key=lambda x: (x[0], x[1]))
    if len(nxt) == 0:   return [-1,-1,-1]
    for f in range(len(fishes)):
        if fishes[f][:2] in nxt and fishes[f][2] < sharkpower:
            return fishes[f]+[cnt]
    visit += nxt
    #print(cnt, visit)
    return target(nxt,fishes,visit,cnt,N,sharkpower,matrix)

N = int(input())
matrix=[]
fishes = []
for i in range(N):
    inp = list(map(int,input().split()))
    for j in range(N):
        if inp[j] == 9:
            shark = [i,j,2,0]
        elif inp[j] > 0:
            fishes.append([i,j,inp[j]])
    matrix.append(inp)
answer = 0
while True:
    nxt = target([[shark[0],shark[1]]], fishes,[], 0,N,shark[2],matrix)
    print(shark, answer)
    if nxt == [-1,-1,-1]:   break
    answer += nxt[3]
    shark[3] += 1
    if shark[2] == shark[3]:
        shark[2] += 1
        shark[3] = 0
    shark[0],shark[1] = nxt[0],nxt[1]
    fishes.remove(nxt[:3])
    print(len(fishes))
print(answer)






'''
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
'''