import itertools

def solution(numbers):
    answer = 0  # 답
    alist = []  # answer이 될 수 있는 후보리스트. 이중 소수인 것을 골라낸다.
    tmp = ''  # 나올 수 있는 녀석들을 tmp에 두고 판단함
    numbers = list(numbers)  # 들어온 문자열을 리스트 형태로 쪼갬
    for i in range(len(numbers)):
        mypermutation = itertools.permutations(numbers, i + 1)  # 길이 1부터 가능한 순열 생성
        for s in mypermutation:  # 순열의 구성원 s
            for k in s:  # s내 각 원소별로
                tmp = str(tmp) + str(k)  # tmp로 빼내기. 바로 str(s) 로의 형변환은 불가. tuple은 안되나봐
            tmp = int(tmp)
            if tmp not in alist and tmp >= 2:
                alist.append(tmp)
            tmp = ''
    flag = 0  # 소수인지를 판단하는 플래그
    for n in alist:
        for i in range(2, n):  # 2부터 n-1까지 나눴을때 나머지가 없으면 소수 아님
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            answer = answer + 1
        flag = 0

    return answer