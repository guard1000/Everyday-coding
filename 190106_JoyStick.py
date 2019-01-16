from string import ascii_uppercase
def solution(name):
    answer = 0
    name = list(name)
    n = len(name)
    state= ['A' for i in range(n)]  #현재 상태 표시
    correct = [0 for i in range(n)]  #각 자리의 문자가 맞는지 여부 1과 0으로 표시
    alpha = list(ascii_uppercase)
    pos = 0     #position. 현재위치
    dis =[0 for i in range(n)]      #이동거리 기준으로 볼 리스트

    #처음부터 맞는 녀석들 있으면 확인해줌
    for i in range(n):
        if state[i] == name[i]:
            correct[i] = 1

    #일단 시작위치에서 바꿔주고 시작
    sb = alpha.index(state[0])
    sa = alpha.index(name[0])
    sc = min(abs(sb-sa), len(alpha)+min(sb,sa)-max(sb,sa))
    answer += sc
    state[0] = name[0]
    correct[0] = 1

    while True:
        #모두 맞게 되면 그만둠
        if sum(correct) == n:
            break
        else:
            cost = [0 for i in range(n)]    # 이동거리(distance)
            for i in range(n):
                # 이동거리는 오른쪽 으로 셀때와 왼쪽으로 이동할때 중 더 짧은 녀석으로
                distance = min(abs(pos-i), n+min(pos, i)-max(pos,i))
                dis[i] = distance

                # 알파벳 변환을 위해서 최소 몇번 변환해야 하는가
                # 알파벳 리스트 상에서 떨어진 거리로 계산. 오른쪽으로 세기와 왼쪽으로 세기 중 작은 것
                before = alpha.index(state[i])
                after = alpha.index(name[i])
                change = min(abs(before-after), len(alpha)+min(before,after)-max(before,after))

                cost[i] = distance + change #각 위치를 변경하는데 필요한 cost 값들이 정리 됨

            #dis 값이 가장 작은 곳으로 pos 이동.



            for i in range(n):
                if correct[i] == 1:
                    dis[i] = 99
            pos = dis.index(min(dis))
            correct[pos] = 1
            state[pos] = name[pos]
            answer += cost[pos]

    return answer




'''
from string import ascii_uppercase
def solution(name):
    answer = 0
    name = list(name)
    n = len(name)
    state= ['A' for i in range(n)]  #현재 상태 표시
    correct = [0 for i in range(n)]  #각 자리의 문자가 맞는지 여부 1과 0으로 표시
    alpha = list(ascii_uppercase)
    pos = 0     #position. 현재위치

    #처음부터 맞는 녀석들 있으면 확인해줌
    for i in range(n):
        if state[i] == name[i]:
            correct[i] = 1

    #일단 시작위치에서 바꿔주고 시작
    sb = alpha.index(state[0])
    sa = alpha.index(name[0])
    sc = min(abs(sb-sa), len(alpha)+min(sb,sa)-max(sb,sa))
    answer += sc
    state[0] = name[0]
    correct[0] = 1
    print(state, sc, answer)

    while True:
        #모두 맞게 되면 그만둠
        if sum(correct) == n:
            break
        else:
            cost = [0 for i in range(n)]    # 이동거리(distance) + 알파벳변환수(change)
            for i in range(n):
                # 이동거리는 오른쪽 으로 셀때와 왼쪽으로 이동할때 중 더 짧은 녀석으로
                distance = min(abs(pos-i), n+min(pos, i)-max(pos,i))

                # 알파벳 변환을 위해서 최소 몇번 변환해야 하는가
                # 알파벳 리스트 상에서 떨어진 거리로 계산. 오른쪽으로 세기와 왼쪽으로 세기 중 작은 것
                before = -1
                after = -1
                for j in range(len(alpha)):
                    if before != -1 and after != -1:
                        break
                    if alpha[j] == state[i]:
                        before = j
                    if alpha[j] == name[i]:
                        after = j
                change = min(abs(before-after), len(alpha)+min(before,after)-max(before,after))

                if correct[i] == 1:     #이미 맞게 설정되어 있다면 임의의 큰값(99) 넣어
                    cost[i] = 99
                else:
                    cost[i] = distance + change #각 위치를 변경하는데 필요한 cost 값들이 정리 됨

            #cost 값이 가장 작은 곳으로 pos 이동.
            pos = cost.index(min(cost))
            correct[pos] = 1
            state[pos] = name[pos]
            answer += cost[pos]
            print(state, cost, answer)

    return answer
'''
n1='JEROEN'
n2='JAN'
n3='JAZ'


print(solution(n1))
print(solution(n2))
print(solution(n3))
