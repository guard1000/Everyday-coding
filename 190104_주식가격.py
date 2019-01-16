'''
def solution(prices):
    answer = []

    while len(prices) > 2:
        for i in range(len(prices) - 1, -1, -1):  # 제일 앞에 값만큼 다 빼줌
            prices[i] = prices[i] - prices[0]

        i = 1
        while i < len(prices):  # 최초로 음수 나오는 곳까지 유지된 것임
            if prices[i] < 0:  # 최초 음수 나온 곳의 인덱스를 answer에 추가
                answer.append(i)
                break
            i += 1
        if i == len(prices):
            answer.append(i-1)
        prices.pop(0)  # 제일 앞에 값 없애줌

    answer.append(1)  # 마지막 두개는 어차피 1과 0
    answer.append(0)

    return answer
'''

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer

p = [498,501,470,489]
print(solution(p))