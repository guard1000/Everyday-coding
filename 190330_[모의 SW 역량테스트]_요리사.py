import itertools
T = int(input())
for t in range(T):
    answer = 1000
    N = int(input())
    mat=[n for n in range(N)]
    table=[]
    for n in range(N):
        table.append(list(map(int,input().split())))
    mycombination = itertools.combinations(mat,len(mat)//2)
    counting = 0
    for combination in mycombination:
        tmp = tuple(set(mat) - set(combination))

        A,B=0,0
        for comb in combination:
            for comb2 in combination:
                if comb != comb2:
                    A += table[comb][comb2]
        for t2 in tmp:
            for t3 in tmp:
                if t2 != t3:
                    B += table[t2][t3]
        if abs(A-B) < answer:
            answer = abs(A-B)

    print('#',end ='')
    print(t+1, end=' ')
    print(answer)








'''
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''