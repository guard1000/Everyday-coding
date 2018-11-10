maps = {}

def dfs(maps, start, search):
    visit = []
    stack = [start, ]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node == search:
                break
            stack.extend([x for x in maps[node] if x not in visit])

    return visit

cnt = int(input('vertex 몇개인가요?: ' ))
for i in range(cnt):
    print(i+1, '번 vertex는 누구와 연결되어 있나요? : ', end='')
    inp = input().split()
    inp = [int(j) for j in inp]
    maps[i+1] = inp

start = int(input('시작점은 어디인가요?: ' ))
search = int(input('찾고자 하는 녀석은 몇번인가요? '))

print(start,'부터', search, '까지 찾아가느 경로는', dfs(maps, start, search), '입니다.')
