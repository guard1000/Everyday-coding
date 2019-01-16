def dfs(rest, computers):  # dfs로 탐색하여 연결된 NW 한 덩어리를 리스트로 뽑아주는 함수
    visit = [rest[0]]  # 남은애들 중 젤 첫번째 애 기준으로 연결된걸 찾아 줌
    stk = []  # 스택처럼 쓸 리스트

    # 방문 안했고, 젤 최근 방문한 녀석에게 연결되어 있으면 stk에 넣어주자
    for i in range(len(computers)):
        if i not in visit and computers[visit[len(visit) - 1]][i] == 1:
            stk.append(i)
    while len(stk) > 0:  # stk가 비어 있다면, 더이상 이 NW 덩어리에 연결된 NW가 없단거니까!
        visit.append(stk[0])  # stk의 가장 앞녀석(스택이니까)을 방문하자. visit에 넣어줌
        stk.pop(0)  # stk 0 번은 visit에 들어갔으니까 없애줘
        for i in range(len(computers)):  # 앞에 한거 반복
            if i not in visit and computers[visit[len(visit) - 1]][i] == 1:
                stk.append(i)
    return visit  # 방문가능한(연결된) NW 한덩어리 반환해 줌


def solution(n, computers):
    answer = 0
    rest = [x for x in range(n)]  # 아직 처리안한 NW들이 있는 리스트
    while len(rest) > 0:  # 모든 NW를 처리할 때 까지
        answer += 1
        tmplist = dfs(rest, computers)  # tmplist 에 dfs의 결과를 저장해서
        cnt = 0  # rest에서 tmplist에 있는 애들을 제거해줌. 매 라운드마다 answer가 올라감
        while cnt < len(rest):  # ㄴ> 매 라운드 마다 NW 덩어리를 카운트하므로!
            if rest[cnt] in tmplist:
                del rest[cnt]
            else:
                cnt += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
