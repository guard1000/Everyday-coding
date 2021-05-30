# 문제: https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# 2020 카카오 인턴십

def solution(gems):
    answer = [0, 100000]
    N = len(gems)
    n_gems = len(set(gems))
    gems_cnt = {gems[0]: 1}

    # edge_case 제거 - 1종류 or N종류
    if n_gems == 1:
        return [1, 1]
    if n_gems == N:
        return [1, n_gems]

    l, r = 0, 0
    while l > -1 and r < N:  # boundary check
        if len(gems_cnt) != n_gems:  # 다 수집 못 했으면 보석줍줍
            r += 1
            if r == N:
                break

            if gems[r] in gems_cnt:
                gems_cnt[gems[r]] += 1
            else:
                gems_cnt[gems[r]] = 1

        else:  # 종류별 수집 되어 있으면 l 을 버려봄
            if r - l < answer[1] - answer[0]:
                answer = [l + 1, r + 1]
            gems_cnt[gems[l]] -= 1
            if gems_cnt[gems[l]] == 0:
                del gems_cnt[gems[l]]  # 0개 되면 삭제
            l += 1

    return answer