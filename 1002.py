import itertools    #모든 조합을 위해!

def solution(numbers):
    answer = 0
    alist = []
    tmp = ''
    numbers = list(numbers)         #입력받은 문자열을 한글자씩 끊어서 리스트로
    for i in range(len(numbers)):   #한자릿수~n자릿수 모든 조합을 구하려고
        mypermutation = itertools.permutations(numbers, i + 1)  #조합구하기
        for s in mypermutation:                         #각 조합에서의 모든 경우에서
            for k in s:
                tmp = str(tmp) + str(k)                 #각 자릿수들을 str으로 바꿔서 연결시킴
            tmp = int(tmp)                              #그리고 다시 정수화
            if tmp not in alist and tmp >= 2:           #중복된 녀석이 없고, 2이상의 수라면 alist에 append
                alist.append(tmp)
            tmp = ''

    flag = 0                    #alist의 원소가 소수인지 아닌지 판단하는 flag변수
    for n in alist:
        for i in range(2, n):   #소수판단
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            answer = answer + 1
        flag = 0

    return answer

numbers='011'
print(solution(numbers))