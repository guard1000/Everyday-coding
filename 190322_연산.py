T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    alist,cnt,nxt=[N],0,[]
    print('#',end ='')
    print(t+1, end =' ')
    i = 0
    while i < len(alist):
        if alist[i]+1 == M or alist[i]-1 ==M or alist[i]*2 ==M or alist[i]-10 == M:    break
        if alist[i]+1 not in alist and alist[i]+1<=1000000 and alist[i]+1 not in nxt: nxt.append(alist[i]+1)
        if alist[i] - 1 not in alist and alist[i]-1 >= 1and alist[i]-1 not in nxt: nxt.append(alist[i] - 1)
        if alist[i] -10 not in alist and alist[i]-10 >=1 and alist[i]-10 not in nxt: nxt.append(alist[i] -10)
        if alist[i] *2  not in alist and alist[i]*2 <=1000000 and alist[i]*2 not in nxt: nxt.append(alist[i] *2)
        i += 1
        if i == len(alist):
            cnt += 1
            alist.extend(nxt)
            nxt.clear()
    print(cnt+1)

'''
1
2 7
'''

'''
def bfs(now,visit,target,cnt):
    for n in now:
        visit.append(n)
        if target == n:
            print(cnt)
            return
    nxt=[]
    for n in now:
        if n-1 not in nxt and n-1 not in visit and n-1 >= 1:
            nxt.append(n-1)
        if n+1 not in nxt and n+1 not in visit and n+1 <= 1000000:
            nxt.append(n+1)
        if n-10 not in nxt and n-10 not in visit and n-10 >= 1:
            nxt.append(n-10)
        if n*2 not in nxt and n*2 not in visit and n*2 <= 1000000:
            nxt.append(n*2)
    bfs(nxt,visit,target,cnt+1)



T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    print('#',end ='')
    print(t+1, end =' ')
    bfs([N],[],M,0)
'''
