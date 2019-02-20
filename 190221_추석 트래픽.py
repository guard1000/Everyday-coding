def check(t, lines):    #몇개 걸치는지 판단하는 함수
    n = len(lines)
    cnt=0
    for line in lines:
        if line[0] > t+999:
            cnt += 1
        elif line[1] < t:
            cnt += 1
    return n-cnt

def solution(lines):
    answer = 0
    for i in range(len(lines)): #각 라인별로 [시작,끝] 꼴로 만들어주고, 시작점 기준 정렬 후 각 시작 끝점을 check해줌
        lines[i] = lines[i][11:-1].split(':')
        lines[i][2]=(lines[i][2].split())
        lines[i].append(lines[i][2][1])
        lines[i][2]=lines[i][2][0]
        lines[i] = [int(lines[i][0])*3600+int(lines[i][1])*60+float(lines[i][2]) ,float(lines[i][3])]
        lines[i] = [(int((lines[i][0]-lines[i][1])*1000+1)) ,(int((lines[i][0])*1000))]
    lines=sorted(lines,key=lambda x: x[0])
    for i in range(len(lines)-1,-1,-1):
        lines[i][1] -= lines[0][0]
        lines[i][0] -= lines[0][0]

    for l in lines:
        if check(l[0],lines) > answer:
            answer = check(l[0],lines)
        if check(l[1],lines) > answer:
            answer = check(l[1],lines)
    return answer

print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))