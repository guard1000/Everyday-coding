import copy

def get_minimum(k, a):  # k : 1, a :(2,3,4) 로 들어온 상황임
    if (k, a) in g: #이미 k 시작해서 a에 있는 원소를 다 도는 경우를 계산해 둔 경우
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]  #그 cost가 반환됨

    values = []
    all_min = []
    for j in a: #(2,3,4)의 원소들이 들어옴
        set_a = copy.deepcopy(list(a))  #a를 list로 바꿔서 deep copy해버림 -> 카피를 바꾸면 원본도 바뀐다.
        set_a.remove(j)     # j 가 2 였다면, set_a는 (3,4) 로 된다.
        all_min.append([j, tuple(set_a)])   #all_min에 [2,(3,4)] 가 들어온다.
        result = get_minimum(j, tuple(set_a))   # result 는 get_minimum([2,(3,4)]) 의 결과값임
        values.append(matrix[k-1][j-1] + result)    #value에 (matix[0][1] + cost) 가 추가됨

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))
    return g[k, a]

g = {}
p = []

T = int(input())
for t in range(T):
    n = int(input())
    matrix =[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))

    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0] #1번(0번인덱스) 아이템으로 바로 가는 cost
    zone=tuple([i for i in range(2,n+1)])
    print(get_minimum(1, zone))
'''
    solution = p.pop()
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                break
    return
'''



