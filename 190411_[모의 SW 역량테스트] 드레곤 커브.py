dir={0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
matrix = [[0 for col in range(101)] for row in range(101)]
K = int(input())
answer = 0
for k in range(K):
    t = list(map(int, input().split()))
    tmp, i = [], 0
    while i <= t[3]:
        if i == 0:  tmp.append(t[2])
        elif i == 1:    tmp.append((t[2] + 1) % 4)
        else:
            n = len(tmp)
            for j in range(int(n / 2)):
                if tmp[j] == 0: tmp.append(2)
                elif tmp[j] == 1:   tmp.append(3)
                elif tmp[j] == 2:   tmp.append(0)
                elif tmp[j] == 3:   tmp.append(1)
            for j in range(int(n / 2), n):
                tmp.append(tmp[j])
        i += 1
    pos = [t[1],t[0]]
    for tp in tmp:
        matrix[pos[0]][pos[1]] += 1
        pos[0] += dir[tp][1]
        pos[1] += dir[tp][0]
        matrix[pos[0]][pos[1]] += 1

for i in range(100):
    for j in range(100):
        if matrix[i][j] != 0 and matrix[i+1][j] != 0 and matrix[i][j+1] != 0 and matrix[i+1][j+1] != 0:
            answer += 1
print(answer)

'''
4
3 3 0 1
4 2 1 3
4 2 2 1
2 7 3 4
'''