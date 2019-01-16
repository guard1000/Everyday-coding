def solution(genres, plays):
    answer = []
    alist = []
    tmp = []
    n = len(genres)
    #곡별 장르-재생횟수 연결해서 alist에 저장
    for x,y in zip(genres, plays):
        alist.append([x,y])
    blist = alist


    #장르순으로 정렬 후, 각 장르별 곡들의 재생횟수를 담자.
    alist = sorted(alist, key=lambda x: x[0])
    i = 0
    while i < n:
        j = i
        tmp.append([alist[i][0]])
        while j < n and alist[i][0] == alist[j][0]:
            tmp[len(tmp)-1].append(alist[j][1]) #재생횟수만 넣자
            j += 1
        i = j
    tmp = sorted(tmp,reverse=True, key=lambda x: sum(x[1:]))
    print(alist)
    print(tmp)

    for i in tmp:
        if len(i) == 2:
            answer.append(blist.index(i))
        else:
            i[1:] = sorted(i[1:], reverse=True)
            for j in range(1,3):
                answer.append(blist.index([i[0],i[j]]))
                blist[answer[len(answer)-1]][1] = -1

    return answer


g=['classic', 'pop', 'classic', 'classic', 'pop']
p=[500, 600, 150, 800, 2500]
g1=['classic','pop','classic','pop','classic','classic']
p1=[400,600,150,2500,500,500]
print(solution(g,p))
print(solution(g1,p1))