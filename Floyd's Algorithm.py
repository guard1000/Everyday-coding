graph=[]
n = int(input("몇개의 Node가 있나요?"))        # 그래프 입력 받기
for i in range(n):
    print(i+1, '번째 노드의 연결상태는? (만약 연결되지 않을경우, 0을 입력)')
    graph.append(list(input().split()))

for i in range(n):          #입력받은 graph의 원소들을 float형으로 변환해주고,
    for j in range(n):
        graph[i][j] = float(graph[i][j])
        if i == j:          #자기 자신에게는 0으로,
            graph[i][j] = 0
        elif graph[i][j] == 0:
            graph[i][j] = 999       #연결이 되지 않은 것은 무한대 대신 그냥 999의 값(엄청 큰 값)을 줌

print("Floyd's Algorithm 적용 전")
print(graph)

for i in range(n):              #플로이드 알고리즘 적용 격자의 겹치는 부분이 두 기준의 합보다 크면 바꿈
    for j in range(n):
        for k in range(n):
            if j != i and k != i and ((graph[j][i] + graph[i][k]) <= graph[j][k]):
                graph[j][k] = graph[j][i] + graph[i][k]

for i in range(n):              #아직 무한
    for j in range(n):
        if graph[i][j] == 999:
            graph[i][j] = 'inf'

print("\nFloyd's Algorithm 적용 후") #출력
for i in range(n):
    for j in range(n):
        if type(graph[i][j]) == float:
            print('%.2f ' %graph[i][j], end = ' ')
        else:
            print(graph[i][j], end= ' ')
    print()