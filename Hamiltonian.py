from string import ascii_uppercase
visited=['A']
stack=[]
graph=[]
answer = ''
alpha = list(ascii_uppercase)   #알파벳 리스트 생성
n = int(input('몇개의 node(vertex)가 있나요?'))
node=alpha[:n] #리스트 슬라이싱으로 노드 완성
for i in range(n):  #graph에 노드 이름 + 연결상태가 들어간 리스트 삽입
    print(node[i], end='')
    inp = input("의 연결상태는? ").split()
    graph.append([alpha[i]])
    for j in inp:
        j = j.upper()
        graph[i].append(j)
#graph의 리스트들은 0번인덱스는 자신, 1번부터는 연결된 애들

for i in range(n):      #연결상태를 작은애들이 뒤에오게끔 정렬 -> stack에 넣기 편하게
    graph[i][1:] = sorted(graph[i][1:], reverse=True)


print(graph)
bt = 0
cnt = 0

while True:

    for i in range(n):
        if graph[i][0] == visited[len(visited)-1]:
            stack.append(graph[i][1:])

    #if stack[len(stack)-1][len(stack[len(stack)-1])-1]

    if len((stack[len(stack)-1])) == 0: # 맨 마지막 리스트 비었으면, 삭제 + 백트래킹
        stack.pop()
        bt = 1

    else:
        tmp = stack[len(stack)-1].pop()
        if len(visited) == n and tmp == 'A':
            visited.append(tmp)

            print('\n끝!')
            print(visited)
            print(cnt)
            break
        while tmp in visited:
            if len(stack[len(stack)-1]) == 0:   #백트레킹
                stack.pop()
                bt=1
                break
            tmp = stack[len(stack)-1].pop()
        answer = tmp
        visited.append(tmp)
        if len(stack[len(stack) - 1]) == 0:  # 백트레킹
            stack.pop()


    if bt == 1:
        while stack[len(stack)-1] == []:
            stack.pop()

        bt =0
        visited = visited[:len(stack)]
        answer = stack[len(stack)-1].pop()
        visited.append(answer)

    print(visited, '         스택:',stack)
    cnt += 1