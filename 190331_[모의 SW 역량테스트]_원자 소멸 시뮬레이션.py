T = int(input())
for t in range(T):
    N = int(input())
    atoms=[]
    for n in range(N):
        atoms.append(list(map(int,input().split())))
    answer , longest = 0, 0
    for i in range(len(atoms)-1):
        for j in range(i+1, len(atoms)):
            if abs(atoms[i][0]-atoms[j][0])+abs(atoms[i][1]-atoms[j][1]) > longest:
                longest = abs(atoms[i][0]-atoms[j][0])+abs(atoms[i][1]-atoms[j][1])

    for r in range(longest):
        if len(atoms) <= 1: break
        for i in range(len(atoms)):
            if atoms[i][2] == 0:    atoms[i][1] += 0.5
            elif atoms[i][2] == 1:  atoms[i][1] -= 0.5
            elif atoms[i][2] == 2:  atoms[i][0] -= 0.5
            elif atoms[i][2] == 3:  atoms[i][0] += 0.5

        atoms = sorted(atoms, key=lambda x: x[:2])
        tmp = set()
        for i in range(len(atoms)-1):
            if atoms[i][0] == atoms[i+1][0] and  atoms[i][1] == atoms[i+1][1]:
                tmp.add(i)
                tmp.add(i+1)
        tmp = list(tmp)
        i = len(tmp)-1
        while i > -1:
            answer += atoms[tmp[i]][3]
            atoms.pop(tmp[i])
            i -= 1
    print('#',end='')
    print(t+1,end=' ')
    print(answer)

'''
T = int(input())
for t in range(T):
    N = int(input())
    atoms=[]
    for n in range(N):
        atoms.append(list(map(int,input().split())))
    answer , longest = 0, 0
    #거리 longest 잡아내기
    for i in range(len(atoms)-1):
        for j in range(i+1, len(atoms)):
            if abs(atoms[i][0]-atoms[j][0])+abs(atoms[i][1]-atoms[j][1]) > longest:
                longest = abs(atoms[i][0]-atoms[j][0])+abs(atoms[i][1]-atoms[j][1])

    tmp = [0 for i in range(len(atoms))]
    for r in range(longest):
        if len(atoms) <= 1: break
        #move()
        for i in range(len(atoms)):
            if atoms[i][2] == 0:    atoms[i][1] += 0.5
            elif atoms[i][2] == 1:  atoms[i][1] -= 0.5
            elif atoms[i][2] == 2:  atoms[i][0] -= 0.5
            elif atoms[i][2] == 3:  atoms[i][0] += 0.5

        #check()
        for i in range(len(atoms)-1):
            for j in range(i+1, len(atoms)):
                if atoms[i][0] == atoms[j][0] and  atoms[i][1] == atoms[j][1]:
                    tmp[i],tmp[j]=r+1,r+1
        for i in range(len(tmp)-1,-1,-1):
            if tmp[i]== r+1:
                answer += atoms[i][3]

    print('#',end='')
    print(t+1,end=' ')
    print(answer)
'''




# 2배로 패딩

# 거리 max*2 만큼 cnt ++


'''
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9
'''