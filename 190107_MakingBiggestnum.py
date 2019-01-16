def solution(number, k):
    answer = ''
    numList = []

    for i, num in enumerate(number):
        while len(numList) > 0 and numList[len(numList) - 1] < num and k > 0:
            numList.pop()
            k -= 1

        numList.append(num)
        if k == 0:
            for j in range(i + 1, len(number)):
                numList.append(number[j])
            break

    answer = ''.join(numList[:len(numList)-k])
    return answer

n1 = '1924'
n2 = '1231234'
n3 = '4177252841'
n4 = '2222222'
print(solution(n1,2))
print(solution(n2,3))
print(solution(n3,4))
print(solution(n4,3))
'''
def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    i = 0

    while True:
        if k <= 0 or i>len(number)-2:
            break

        elif number[i:i + k + 1].index(max(number[i:i + k + 1])) != 0:  # i~i+k 사이에 최댓값이 0번 인덱스가 아니면
            cnt = number[i:i + k + 1].index(max(number[i:i + k + 1]))
            k = k - cnt
            number = number[:i] + number[i + cnt:]

        else:
            i += 1
        n = len(number)

    for i in range(k):
        number.pop(number.index(min(number)))

    for i in number:
        answer += str(i)
    return answer
'''

n1 = '1924'
n2 = '1231234'
n3 = '4177252841'
n4 = '2222222'
print(solution(n1,2))
print(solution(n2,3))
print(solution(n3,4))
print(solution(n4,3))
