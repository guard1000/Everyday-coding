dic ={'0': 0,'1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}
def val(target):
    v,hexa = dic[target[-1]],16
    for l in range(-2, -len(target)-1,-1):
        v += hexa*dic[target[l]]
        hexa *= 16
    return v

T = int(input())
for t in range(T):
    N,K = map(int, input().split())
    n = N//4
    inp = list(input())
    inp = inp+inp[:n]
    candi=set()

    for cnt in range(n):
        box, j = [], 0
        for i in range(4):
            box.append(inp[cnt+j:cnt+j + n])
            j += n
        for bo in box:
            candi.add(tuple(bo))
    candi = sorted(list(candi), reverse=True, key=lambda x: val(x))
    print('#',end='')
    print(t+1,end=' ')
    print(val(candi[K-1]))



'''
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99
'''