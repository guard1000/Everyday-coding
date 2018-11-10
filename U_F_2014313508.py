#2014313508 박천욱
import csv

def findF_cc(s):
    score = 14-s
    if score < 4:
        return 100-(score*5)
    else:
        return 0

def findF_HW(s):
    score = 22-s
    if score <= 3:
        return 100-(score*5)
    else:
        return 0

def findF_MT(s):
    if s >= 60:
        return s
    else:
        return 0

def findF_Q(s):
    if s >= 80:
        return s
    else:
        return 0

def findF_F(s):
    if s >= 60:
        return s
    else:
        return 0

def goF(flist, inplist):
    for target in flist:
        if target in inplist:
            inplist.remove(target)

inp = []
flist = []
cnt = 0
f = open('데이터셋.csv', 'r')   #파일열어서 inp 리스트로 받음
rdr = csv.reader(f)
for line in rdr:
    if cnt > 0:
        inp.append(line)
        for j in range(1,6):
            inp[cnt-1][j] = int(inp[cnt-1][j])
    cnt += 1
f.close()
A = int(len(inp)*0.5)
B = int(len(inp)*0.4)   #성적계산용
C = int(len(inp)*0.1)

for i in range(len(inp)):       #1번조건 출석
    score = findF_cc(inp[i][1])
    if score == 0:
        flist.append(inp[i])    #출석 부적격적들 flist로
    else:
        inp[i][1] = score

goF(flist, inp)                 #flist는 이제부터 보지 않는다. inp에서 제거


for i in range(len(inp)):       #2번조건 과제
    score = findF_HW(inp[i][2])
    if score == 0:
        flist.append(inp[i])    #과제 부적격적들 flist로
    else:
        inp[i][2] = score

goF(flist, inp)                 #flist는 이제부터 보지 않는다. inp에서 제거


for i in range(len(inp)):       #3번조건 중간고사
    score = findF_MT(inp[i][3])
    if score == 0:
        flist.append(inp[i])    #과제 부적격적들 flist로
    else:
        inp[i][3] = score

goF(flist, inp)                 #flist는 이제부터 보지 않는다. inp에서 제거


for i in range(len(inp)):       #4번조건 퀴즈
    score = findF_Q(inp[i][4])
    if score == 0:
        flist.append(inp[i])    #과제 부적격적들 flist로
    else:
        inp[i][4] = score

goF(flist, inp)                 #flist는 이제부터 보지 않는다. inp에서 제거


for i in range(len(inp)):       #5번조건 기말고사
    score = findF_F(inp[i][5])
    if score == 0:
        flist.append(inp[i])    #과제 부적격적들 flist로
    else:
        inp[i][5] = score

goF(flist, inp)                 #flist는 이제부터 보지 않는다. inp에서 제거


result = sorted(inp, reverse = True, key=lambda x:sum(x[1:])) #1번 인덱스값을 기준으로 소팅할때 람다

if len(flist) > B + C:      #B, C 보다 F가 많으면, 살아남은사람 다 A+ 나머지 F
    for i in result:
        print(i[0], ':', 'A+')
    for j in flist:
        print(j[0], ':', 'F')

elif len(flist) > C:        #C보다 F가 많으면, 살아남은이들중 A+,B+, 그외 F
    c = 0
    for i in result:
        if c < A:
            print(i[0], ':', 'A+')
        else:
            print(i[0], ':', 'B+')
        c += 1
    for j in flist:
        print(j[0], ':', 'F')

else:       #그외: C보다 F가 적어
    c = 0
    for i in result:
        if c < A:
            print(i[0], ':', 'A+')
        elif c < A+B:
            print(i[0], ':', 'B+')
        else:
            print(i[0], ':', 'C+')
    for j in flist:
        print(j[0], ':', 'F')