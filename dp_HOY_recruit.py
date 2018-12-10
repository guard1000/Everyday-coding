#2014313508 박천욱
import csv

inp = []
cnt = 0
max_size=[5,10,3,5]
dept =[]
deptlist=[[],[],[],[]]  #5 10 3 5
deptrest=[]
answer=0

def calcM():    #M 계산함수
    M=0
    for m in range(5):
        M = M+dept[m][1]
    for m in range(5,15):
        M = M+dept[m][2]
    for m in range(15,18):
        M = M+dept[m][3]
    for m in range(18,23):
        M = M+dept[m][4]
    return M

f = open('data_dp.csv', 'r')   #파일열어서 inp 리스트로 받음 101명의 데이터가 있음
rdr = csv.reader(f)
for line in rdr:
    inp.append(line)
    for j in range(1,6):
        inp[cnt][j] = int(inp[cnt][j])
    cnt += 1
f.close()

n = int(input("지원자는 몇명인가요?: (단, 100명 이하, 23명 이상)"))     #inp로 읽어온 데이터 중 몇명까지 사용할지 입력받음
inp = inp[:n]   #리스트 슬라이싱으로 사용할 데이터 셋 완성

#이제 서류 인성 적성 면접 개발 점수를 토대로 점수를 만들어보자.
for i in range(n):
    H = inp[i][2]   #인사부 점수 -> 인성점수 100%
    P = inp[i][5]   #개발부 점수 -> 개발점수 100%
    S = inp[i][1]*0.15 + inp[i][2]*0.15 + inp[i][3]*0.2 + inp[i][4]*0.1 + inp[i][5]*0.4     #전략&기획부서 점수
    F = inp[i][1]*0.2 + inp[i][2]*0.2 + inp[i][3]*0.4 + inp[i][4]*0.2   #재경부서 점수
    inp[i] = [inp[i][0], H, P, S, F]    #inp를 조정된 값으로 수정

    # inp에는 ['이름', H, P, S, F] 의 형태로 저장되어 있으므로, inp[i][1:]로 슬라이싱하여 [H, P, S, F]의 값들에 집중해보자.
    # 아래는 HPSF중 가장 작은 값을 가지는 인덱스 부터 큰 값을 가지는 녀석의 인덱스 순으로 정렬했다.
    # 예) [27, 77, 56, 43] 이라면 index=[0, 3, 2, 1]으로 정렬함.
    index = sorted(range(len(inp[i][1:])), key=lambda a: inp[i][1:][a])
    deptlist[index[3]].append(inp[i])


#정렬. 자기 부서에서 필요한 점수대 기준으로 내림차순
for i in range(4):
    deptlist[i] = sorted(deptlist[i], reverse= True, key=lambda x:x[i+1])

for i in range(4):          #범위를 넘어가는 애들은 일단 잘라내둠.
    if len(deptlist[i]) > max_size[i]:
        deptlist[i] = deptlist[i][:(max_size[i])]


#아직 deptlist에 포함되지 못한애들은 일단 deptrest 리스트로
tmp=[]
for i in range(4):
    for j in range(len(deptlist[i])):
        tmp.append(deptlist[i][j])

for i in inp:
    if i not in tmp:
        deptrest.append(i)


#deptrest에서 일단 각 영역별 점수 높은 애들을 해당 부서로 넣어 줌
for i in range(4):
    if len(deptlist[i]) < max_size[i]:
        for j in range(max_size[i]-len(deptlist[i])):   # 몇개가 더 들어가야 하는지 계산해서 그만큼 추가해줌
            deptlist[i].append(sorted(deptrest, reverse= True, key=lambda x:x[i+1])[j])


for i in range(4):       #이제 초기화 된 dept 생성
    for j in deptlist[i]:
        dept.append(j)

print("그리디하게 초기화한 결과")
print(dept)         #초기화 된 dept  출력
answer = calcM()
print(answer)  #초기화 된 dept의 M 계산 결과 출력
print()

deptrest.clear()        #deptrest에 아직 못들어간 애들을 일단 다 넣어둠
for i in inp:
    if i not in dept:
        deptrest.append(i)

# 이제 비교해보자
for i in range(n):
    if inp[i] not in dept:
        for j in range(23):
            flag = 0
            temp = dept[j]      #잠시 보관
            dept[j] = inp[i]
            for a in range(22):
                for b in range(a+1, 23):
                    dept[a],dept[b] =dept[b],dept[a]
                    if calcM() <= answer:
                        dept[a], dept[b] = dept[b], dept[a]
                    else:
                        flag = 1
                        answer = calcM()

            if flag != 1:
                dept[j] = temp

    if inp[i] in dept:
        for a in range(22):
            for b in range(a + 1, 23):
                dept[a], dept[b] = dept[b], dept[a]
                if calcM() <= answer:
                    dept[a], dept[b] = dept[b], dept[a]
                else:
                    answer = calcM()
print("최종 입사자 명단")
print(dept)
print(answer)












'''
    #inp에는 ['이름', H, P, S, F] 의 형태로 저장되어 있으므로, inp[i][1:]로 슬라이싱하여 [H, P, S, F]의 값들에 집중해보자.
    #아래는 HPSF중 가장 작은 값을 가지는 인덱스 부터 큰 값을 가지는 녀석의 인덱스 순으로 정렬했다.
    # 예) [27, 77, 56, 43] 이라면 index=[0, 3, 2, 1]으로 정렬함.
    index = sorted(range(len(inp[i][1:])), key=lambda a: inp[i][1:][a])

    if len(answer[index[3]]) < max_size[index[3]]:
        answer[index[3]].append(inp[i])
    elif
'''

'''
#인사부부터 넣어보자
h_base = sorted(inp, reverse = True, key=lambda x:(x[2]))
for i in range(5):
    hlist.append(h_base[i])
    h_base.pop(0)

#개발부
p_base = sorted(inp, reverse = True, key=lambda x:(x[5]))
for i in range(5):
    plist.append(p_base[i])
    p_base.pop(0)
    '''
