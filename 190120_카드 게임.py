def solution(left, right):
    n =len(left)
    score = [[0 for cols in range(n+1)] for rows in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if left[i-1] > right[j-1]:  # 지금 왼쪽이 더 클때 -> 오른쪽 버릴 수 있음
                #이전에서 양쪽 다 버릴때, 왼쪽만 버릴때, 오른쪽만 버릴때 의 경우 중 젤 큰거 고르면 됨.
                score[i][j] = max(score[i-1][j-1], score[i-1][j], score[i][j-1]+right[j-1])
            else:   #오른쪽이 더 크거나 같을때
                score[i][j] = max(score[i - 1][j - 1], score[i - 1][j])  # 이전에서 둘다 버린것과 왼쪽만 버린 것 중에 큰거
    return score[n][n]

'''
# DFS, branch&bound 활용
def BB(left, right, l, r, answer,tmp,visit):
    stk=[]
    if [l,r] not in visit and left[l] > right[r]:
        visit.append([l,r])
        for i in range(2,-1,-1):
            stk.append(i)
    elif [l,r] not in visit and left[l] <= right[r]:
        visit.append([l,r])
        for i in range(1,-1,-1):
            stk.append(i)



    while stk:
        print('l=', l, 'r=', r, '\n', 'stk=', stk, 'tmp=', tmp, '\n', 'visit=', visit, answer, '\n')

        nxt=stk.pop()

        if nxt == 0:    #0이면 왼쪽을 버림
            if r < len(right)-1 and l <len(left)-1 and tmp + sum(right[r+1:]) > answer:
                return BB(left,right,l+1,r,answer,tmp,visit)

        elif nxt == 1:  #1이면 왼쪽 오른쪽 다 버림
            if r < len(right)-1 and l <len(left)-1 and tmp + sum(right[r+1:]) > answer:
                return BB(left,right,l+1,r+1,answer,tmp,visit)

        elif nxt == 2: #2이면 오른쪽만 버림
            tmp += right[r]
            if r < len(right) - 1 and tmp + sum(right[r + 1:]) > answer:
                return BB(left,right,l,r+1,answer,tmp,visit)

        if tmp > answer:
            answer = tmp



def solution(left, right):
    answer = 0
    l,r = 0,0 #left와 right의 인덱스를 가리킬 변수
    stk=[]
    tmp =0
    visit=[]
    answer = BB(left, right, l, r, answer,tmp,visit)
    return answer
'''
l=[3, 2, 5]
r=[2, 4, 1]
print(solution(l,r))