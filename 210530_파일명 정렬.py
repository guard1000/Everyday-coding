# 문제: https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3
# 2018 KAKAO BLIND RECRUITMENT

import string

def solution(files):
    answer = []
    targets = []
    nums, no_nums = list(string.digits), list(string.ascii_letters) + [' ', '.', '-']
    split_idx_1 = 0

    # split
    idx = 0
    for file in files:
        for _ in range(len(file)):
            if file[_] in nums:
                split_idx_1 = _
                break
        split_idx_2 = split_idx_1
        while split_idx_2 < len(file):
            if file[split_idx_2] in no_nums:
                break
            split_idx_2 += 1

        # targets에 삽입
        HEAD = file[:split_idx_1]
        NUM = file[split_idx_1:split_idx_2]
        targets.append([HEAD.lower(), int(NUM), idx])
        idx += 1

    # sorting
    targets = sorted(targets, key=lambda x: (x[0], x[1]))  # 기준소팅
    for target in targets:
        answer.append(files[target[2]])

    return answer