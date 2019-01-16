def solution(priorities, location):
    answer = 0
    alist=[]        # 입력시의 priority와 location들을 매치하여 저장할 리스트
    for i in range(len(priorities)):
        alist.append([priorities[i], i])


    for i in range(len(alist)**2):

        tmp = alist[0]
        j=1             # 1번부터 보면서 더 큰놈 있나 찾아봄
        while j < len(alist):
            if alist[j][0] > tmp[0]:
                break
            j += 1
        if j == len(alist):    # 이번 문서보다 우선순위가 큰놈이 없다는 거 - 출력
            answer += 1
            if tmp[1] == location:
                return answer
            else:
                alist.pop(0)
        else:                       # 이번 문서보다 우선순위가 큰 놈이 큐에 있네
            alist.pop(0)
            alist.append(tmp)



p1 = [2, 1, 3, 2]
l1 = 2
p2 = [1, 1, 9, 1, 1, 1]
l2 = 0

print(solution(p1, l1))
print(solution(p2, l2))
