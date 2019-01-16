def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1]) #나가는 순간 기준으로 정렬
    flag = [0 for i in range(len(routes))]
    i=0
    while i < len(routes):
        if flag[i] == 0:
            answer += 1
            e = routes[i][1]    #나가는 순간
            for j in range(i, len(routes)):
                if flag[j] == 0 and routes[j][0] <= e:
                    flag[j] = 1
        i += 1

    '''
    while len(routes) > x:
        if flag[x] == 0:
            answer += 1
            flag[x] = 1
            s = routes[x][0]    #start
            e = routes[x][1]    #end
            for i in range(len(routes)-1,x,-1):
                if (routes[i][0] > e or routes[i][1] < s):
                    continue
                else:
                    flag[i] = 1
        x += 1
    '''
    return answer


r=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(r))