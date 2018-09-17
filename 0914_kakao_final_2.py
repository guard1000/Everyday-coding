num = int(input())
inp = []
money = 0
alist = []

def gcd(a, b):                  #gcd 함수
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

for i in range(num):
    inp.append(list(input().split()))

for i in range(num):                            #입금일 경우
    if int(inp[i][0]) > 0:
        money = money + int(inp[i][0])

    else:
        if money + int(inp[i][0]) >= 0: #잔고가 지출보다 많을경우
            money = money + int(inp[i][0])
        else:                           #잔고가 지출보다 적을경우 -> 충전해야해
            charge = int(inp[i][1]) - int(inp[i][0]) - money        #그때 총 충전된 량을 charge로 구함
            alist.append(charge)
            money = int(inp[i][1])

n = len(alist)
blist=[]
if n == 0:
    print(-1)
elif n == 1:
    print(alist[0])
else:
    blist.append(alist[0])
    for i in range(n-1):
        blist.append(gcd(int(blist[i]),int(alist[i+1])))

    if blist[len(blist)-1] == 1:
        print(-1)
    else:
        print(blist[len(blist)-1])

