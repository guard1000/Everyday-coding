def solution(progresses, speeds):
    answer = []
    able = []   # 몇일 후부터 배포 가능한지 저장하는 리스트
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:    # ex) n일 으로 딱 나눠 떨어지게 걸리지 않고 n.2일 이런식으로 나오면
            able.append(((100-progresses[i]) // speeds[i]) + 1)     # ㄴ> n+1일 걸리는 거임
        else:       # 이 speed로 딱 n일 걸린다고 맞아 떨어지면 n 추가
            able.append((100-progresses[i]) // speeds[i])

    i=0
    while i < len(able)-1:
        cnt = 1
        while i+cnt < len(able)-1 and able[i+cnt] <= able[i]:
            cnt += 1
        answer.append(cnt)
        i = i+cnt

    if i == len(able) - 1:
        answer.append(1)

    return answer

p=[93,30,55]
s=[1,30,5]
p2=[93,30,55,10,10,10,10]
s2=[1,30,5,5,8,3,3]
print(solution(p,s))
print(solution(p2,s2))