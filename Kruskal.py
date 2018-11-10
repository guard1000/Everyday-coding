from string import ascii_uppercase

graph=[]    #그래프
visited=[]  #방문한 노드 기록용
answer=[]

def Kruskal(kru, n):
    kru = sorted(kru, key=lambda x: x[2])
    for x in kru:
        if len(visited) == n:
            ans=[]
            for j in range(len(answer)):
                ans += answer[j]
            print(ans)
            return 0
        if x[0] not in visited and x[1] not in visited:
            answer.append([x[0],x[1]])
            visited.append(x[0])
            visited.append(x[1])
        elif x[0] not in visited and x[1] in visited:
            visited.append(x[0])
            for y in answer:
                if x[1] in y:
                    y.append(x[0])
        elif x[1] not in visited and x[0] in visited:
            visited.append(x[1])
            for y in answer:
                if x[0] in y:
                    y.append(x[1])
        print(answer)




        if x[1] not in visited:
            visited.append(x[1])



alpha = list(ascii_uppercase)   #알파벳 리스트 생성
n = int(input('몇개의 node(vertex)가 있나요?'))
node=alpha[:n] #리스트 슬라이싱으로 노드 완성
print('node\n', node)

print('연결상태를 입력해주세요.')
print('입력 예시: A B 5')
print('만약 그만 입력하고자 하면 -1 입력')
while True:
    inp = input('입력: ')
    if inp == '-1':
        break
    else:
        inp = inp.split()
        inp[2] = int(inp[2])
        if inp[0] in node and inp[1] in node:
            graph.append(inp)

print('그래프 형태는 다음과 같습니다.\n', graph)
Kruskal(graph, n)







