# Nat = input().split()                   #나라 입력받음
# inp.append(list(input().split()))
# n, t, m, p = map(int, input().split())

def solution(record):
    answer = []
    inp=[]
    n = 0

    for s in record:
        inp.append(list(s.split()))

    n = len(inp)
    for i in range(n):
        if inp[i][0] == 'Enter':    #만약 Enter라면
            for j in range(i):      #i까지 돌면서 같은 아이디의 닉네임을 다 바꿔줌
                if inp[j][1] == inp[i][1]:
                    inp[j][2] = inp[i][2]
        elif inp[i][0] == 'Leave': #만약 Leave라면
            for j in range(i):      #i까지 돌면서 같은 아이디의 닉네임을 추가시켜줌
                if inp[j][1] == inp[i][1]:
                    inp[i].append(inp[j][2])
        elif inp[i][0] == 'Change': #만약 Change 라면
            for j in range(i):      #i까지 돌면서 같은 아이디의 닉네임을 바꿔줌
                if inp[j][1] == inp[i][1]:
                    inp[j][2] = inp[i][2]

    for k in range(n):
        if inp[k][0] == 'Enter':    #엔터이면
            answer.append(inp[k][2]+'님이 들어왔습니다.')
        elif inp[k][0] == 'Leave':    #Leave이면
            answer.append(inp[k][2] + '님이 나갔습니다.')

    return answer

#
record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo','Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']

print(solution(record))
#