T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flag = [1 for n in range(N)]
    tmplist = list(map(int, input().split()))
    inp = []
    i = 0
    while i < len(tmplist):  # 2씩 쌍 만들기
        inp.append([tmplist[i], tmplist[i + 1]])
        i += 2
    i = 0
    while i < len(inp):
        j = i + 1
        while j < len(inp):
            ni,nj = len(inp[i]),len(inp[j])
            tmp=inp[i][:]
            tmp.extend(inp[j])
            tmp=list(set(tmp))
            if len(tmp) < ni + nj:
                inp[i] = tmp
                inp.pop(j)
                j = i
            j += 1
        i += 1

    for ip in inp:
        for i in ip:
            flag[i-1] = 0
    print('#',end='')
    print(t+1,end=' ')
    print(len(inp)+sum(flag))

