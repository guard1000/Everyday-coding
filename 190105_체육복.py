def solution(n, lost, reserve):
    answer = 0
    cnt=0
    #student 리스트 만들어서 보유상황 표시
    student = [1 for i in range(n)]

    for i in reserve:
        student[i-1] += 1
    for i in lost:
        student[i-1] -= 1

    #2개인 놈들이 빌려주자.
    if student[0] == 2 and student[1] == 0: #양 끝단 처리
        student[0] = 1
        student[1] = 1
    if student[n-1] == 2 and student[n-2] == 0: #양 끝단 처리
        student[n-1] = 1
        student[n-2] = 1
    for i in range(1, n-1):                     #내부 처리
        if student[i] == 2 and student[i+1] == 0:
            student[i] = 1
            student[i+1] =1
        elif student[i] == 2 and student[i-1] == 0:
            student[i] = 1
            student[i-1] = 1
    for i in range(n):
        if student[i] == 0:
            cnt += 1
    answer = n - cnt
    print(student)
    return  answer

'''
def solution(n, lost, reserve):
    answer = 0
    rent = 0    #빌려 받을 수 있는 애들 수
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in lost:  #도난 당핸 애들 중 앞이나 뒤가 reserve면 빌릴 수 있음
        if i-1 in reserve:
            rent += 1
            reserve.remove(i-1) 
        elif i+1 in reserve:
            rent += 1
            reserve.remove(i+1)
    answer = n - len(lost) + rent

    return answer
'''

'''
def solution(n, lost, reserve):
    answer = 0
    #1번과 n번 처리
    if 1 not in lost:
        answer += 1
    elif 2 in reserve:
        answer += 1
        reserve.remove(2)
    if n not in lost:
        answer += 1
    elif n-1 in reserve:
        answer += 1
        reserve.remove(n-1)

    #2번부터 n-1번까지
    for i in range(1,n-1):
        if i+1 not in lost:
            answer += 1
        elif i in reserve:
            answer += 1
            reserve.remove(i)
        elif i+2 in reserve:
            answer += 1
            reserve.remove(i+2)

    return answer
'''

n1=5
l1=[2,4]
r1=[1,3,5]
n2=5
l2=[2,4]
r2=[3]
print(solution(n1, l1, r1))
print(solution(n2, l2, r2))

