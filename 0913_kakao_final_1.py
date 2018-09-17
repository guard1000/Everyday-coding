import copy

Nat = input().split()                   #나라 입력받음
l = [[0]*4 for i in range(4)]

for c in range(6):
    inp = input().split()           #인풋받자

    for i in range(4):              #각각 어떤나가 어떤 나라에 대하여의 확률인지 i와 j로 찾음
        if inp[0] == Nat[i]:
            break
    for j in range(4):
        if inp[1] == Nat[j]:
            break
    l[i][j] = float(inp[2])*3 + float(inp[3])       #i가 j에 대해 얻는 기댓값 계산
    l[j][i] = float(inp[4])*3 + float(inp[3])       #j가 i에 대해 얻는 기댓값 계산

alist = []
for i in range(4):                      #alist에 각각의 점수 기댓값의 합 으로 최종 기댓값 구해줌
    sum = 0
    for j in range(4):
        sum = sum + float(l[i][j])
    alist.append(sum)

blist = copy.copy(alist)            #blist에 alist를 복제해서 sort로 오름차순 정렬
blist.sort()


if blist[1]==blist[2]:                              # alist녀석들을 진출확률로 바꿔주기. 이건 좀더 잘만들 수 있을거 같은데..
    if blist[0]==blist[1] and blist[2]==blist[3]:
        for i in range(4):
            alist[i] = 1/4

    elif blist[2]==blist[3]:
        for i in range(4):
            if alist[i] == blist[0]:
                alist[i] = 0
            else:
                alist[i] = 1/3
    elif blist[0]==blist[1]:
        for i in range(4):
            if alist[i] == blist[3]:
                alist[i] = 1
            else:
                alist[i] = 1 / 3
    else:
        for i in range(4):
            if alist[i] == blist[3]:
                alist[i] = 1
            elif alist[i] == blist[2]:
                 alist[i] = 1/2
            elif alist[i] == blist[1]:
                alist[i] = 1/2
            else:
                alist[i] = 0

else:
    for i in range(4):
        if alist[i] == blist[3] or alist[i] == blist[2]:
            alist[i] = 1
        else:
            alist[i] = 0

for i in range(4):                      #출력
    print('%0.6f' %float(alist[i]))

