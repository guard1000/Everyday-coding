import copy
def spring(A,forest):
    forest = sorted(forest, key = lambda x: (x[:2], x[3]))
    for f in range(len(forest)):
        if forest[f][2] > A[forest[f][0]][forest[f][1]]:    #못먹음 -> die
            forest[f][3] = 1    #die 표기
        else:
            A[forest[f][0]][forest[f][1]] -= forest[f][2]   #양분 쪼옥
            forest[f][2] += 1   #나이 +1
    return A,forest

def summer(A,forest):
    death=[0 for i in range(len(forest))]
    for f in range(len(forest)):
        if forest[f][3] == 1:    #이번에 죽은 나무
            death[f] = 1
            A[forest[f][0]][forest[f][1]] += forest[f][2]//2    #양분 주자
    for i in range(len(death)-1,-1,-1): #나무 제거
        if death[i] == 1:
            forest.pop(i)
            death[i] = 0
    return A, forest

def fall(A,forest):
    baby=[]
    for tree in forest:
        if tree[2] % 5 == 0:    #번식
            if A[tree[0]-1][tree[1]-1] != -1:    baby.append([tree[0]-1,tree[1]-1,1,0])
            if A[tree[0] - 1][tree[1]] != -1:    baby.append([tree[0] - 1, tree[1], 1, 0])
            if A[tree[0] - 1][tree[1]+1] != -1:    baby.append([tree[0] - 1, tree[1]+1, 1, 0])
            if A[tree[0]][tree[1]-1] != -1:    baby.append([tree[0], tree[1]-1, 1, 0])
            if A[tree[0]][tree[1]+1] != -1:    baby.append([tree[0], tree[1]+1, 1, 0])
            if A[tree[0] + 1][tree[1]-1] != -1:    baby.append([tree[0] + 1, tree[1]-1, 1, 0])
            if A[tree[0] + 1][tree[1]] != -1:    baby.append([tree[0] + 1, tree[1], 1, 0])
            if A[tree[0] + 1][tree[1]+1] != -1:    baby.append([tree[0] + 1, tree[1]+1, 1, 0])
    forest += baby
    return A, forest

def winter(A, B):
    for row in range(1,N+1):
        for col in range(1,N+1):
            A[row][col] += B[row][col]
    return A, B


N,M,K = map(int, input().split())
A,forest=[],[]
A.append([-1 for i in range(N+2)])
for n in range(N):
    A.append([-1]+list(map(int,input().split()))+[-1])
A.append([-1 for i in range(N+2)])
B = copy.deepcopy(A)
for i in range(1, N+1):
    for j in range(1, N+1):
        A[i][j] = 5
for m in range(M):
    forest.append(list(map(int, input().split()))+[0])


for k in range(K):
    A, forest = spring(A,forest)
    A, forest = summer(A,forest)
    A, forest = fall(A,forest)
    A, B = winter(A,B)
print(len(forest))

'''
5 2 6
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
'''