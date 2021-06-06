from collections import Counter

def solution(a):
    answer = -1

    # 짝 못이룰 경우 처리
    if len(a) < 2:
        return 0

    # counter dic 생성 - most_common으로 빈도순 정렬
    counts = Counter(a).most_common()

    for key, val in counts:
        # val * 2 가 answer보다 작거나 같을 경우 무시
        if val * 2 <= answer:
            continue

        tmp = 0
        idx = 0
        while idx < len(a) - 1:
            # 조건1: 집합 내 서로 다른 값이어야 함
            # 조건2: 집합 내 val을 포함하고 있어야 함
            if (
                    (a[idx] == a[idx + 1]) or
                    (a[idx] != key and a[idx + 1] != key)
            ):
                idx += 1
                continue
            tmp += 2
            idx += 2

        if answer < tmp:
            answer = tmp

    return answer