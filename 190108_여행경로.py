candidates = []
def visit(start, graph, visited, cnt, route):
    global candidates
    if cnt == len(graph):
        candidates.append(route.split(" "))
    else:
        for i in range(len(graph)):
            if visited[i] == 0 and graph[i][0] == start:
                go = []
                for j in range(len(visited)):
                    go.append(visited[j])
                go[i] = 1
                visit(graph[i][1], graph, go, cnt+1, route+" "+graph[i][1])

def solution(tickets):
    answer = []
    tickets.sort()
    visited = [0] * len(tickets)
    visit("ICN", tickets, visited, 0, "ICN")
    return candidates[0]

'''
alpha = []
def dfs(graph, answer, num, start):
    stk=[]
    global alpha
    if len(answer) == num:
        alpha.append(answer[:])
        return answer
    for i in range(len(graph)-1,-1,-1):
        if graph[start][i] == 1 and ([start, graph[start][i]] not in answer):
            stk.append(i)
    while len(stk) > 0:
        nxt = stk.pop()
        if [start,nxt] not in answer:
            answer.append([start,nxt])
            dfs(graph, answer, num, nxt)
    answer.pop()

def solution(tickets):
    answer = []
    #1. 전체 공항들 이름 순으로 정렬된 리스트 만들기
    #인천공항은 젤 앞에 있음
    airport = []
    for i in tickets:
        airport.append(i[0])
        airport.append(i[1])
    airport = sorted(list(set(airport)))    # set으로 갔다가 오면, 중복이 자연스럽게 제거됨
    airport.remove('ICN')
    airport = ['ICN'] + airport

    #2. 위에서 만든 공항 리스트로 <'공항명' : 인덱스번호> 꼴로 딕셔너리 생성
    az = dict(zip(airport,range(len(airport))))

    num = len(tickets)  #ticket 갯수. num의 depts까지 가면 결과 return 시킬 것임
    n = len(airport)    #공항 갯수 몇개인지

    #3. ticket 정보 기반으로 2차원 배열 만들기 - graph
    graph = [[0 for rows in range(n)]for cols in range(n)]
    for i in range(num):    #ticket 수만큼 edge 생성
        graph[az[tickets[i][0]]][az[tickets[i][1]]] += 1  #az딕셔너리를 이용해 도시이름을 바로 index로 매칭가능
    dfs(graph, answer, num,0)
    answer = alpha

    #공항리스트에서 해당되는 인덱스의 영문 이름으로 치환
    for i in range(len(answer)):
        answer[i] = airport[answer[0][i][1]]

    return answer
'''

'''
def available(a, b, n): #변환 가능한지 여부를 반환
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    if cnt == n-1:
        return True
    return False

def bfs(begin, target, words, answer):
    answer += 1
    tmp =[]
    n = len(begin)      #단어 길이
    if begin in words:
        words.remove(begin)
    for i in words:
        if available(begin, i, n):
            tmp.append(i)
    if target in tmp:
        return answer
    for i in tmp:
        return bfs(i, target, words, answer)

def solution(begin, target, words):
    answer = 0
    begin = list(begin)
    target = list(target)
    num = len(words)    #단어 갯수
    for i in range(num):     #word 리스트 정리
        words.append(list(words[0]))
        words.pop(0)

    answer = bfs(begin, target, words,answer)
    if not answer:
        answer = 0
    return answer
'''
t1=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
t2=[['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
t3=[['ICN', 'AAA'], ['ICN', 'BBB'], ['BBB', 'ICN']]
t4=[['ICN', 'AAA'], ['ICN', 'BBB'],['BBB', 'CCC'],['BBB', 'DDD'],['DDD', 'BBB'], ['CCC', 'ICN']]
print(solution(t1))
print(solution(t2))
print(solution(t3))
print(solution(t4))