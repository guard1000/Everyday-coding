# 문제: https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3
# 월간 코드 챌린지 시즌2

def solution(numbers):
    answer = []
    for num in numbers:
        num = bin(num)[2:]
        # print(num, num[1],len(num))

        # 1. 가장 작은 자릿수의 '0' 탐색
        zero_idx = len(num) - 1
        while zero_idx >= 0 and num[zero_idx] == '1':
            zero_idx -= 1

        # 1-1. 전부 1로 채워진 경우 -> 가장 큰 자릿수의 '1'을 '10'으로 수정
        if zero_idx == -1:
            num = '10' + num[1:]

            # 2. 탐색된 0을 1로 수정 후 그보다 작은 자릿수들 중 가장 큰 자릿수의 '1'을 '0'으로 수정
        else:
            num = num[:zero_idx] + '1' + num[zero_idx + 1:]

            one_idx = zero_idx + 1
            while one_idx < len(num) and num[one_idx] == '0':
                one_idx += 1
            # 1 -> 0 수정
            if one_idx != len(num):
                num = num[:one_idx] + '0' + num[one_idx + 1:]

        answer.append(int('0b' + num, 2))

    return answer