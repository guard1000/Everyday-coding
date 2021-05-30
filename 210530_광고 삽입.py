# 문제: https://programmers.co.kr/learn/courses/30/lessons/72414
# 2021 KAKAO BLIND RECRUITMENT

def solution(play_time, adv_time, logs):
    answer = 0
    # 입력 받은 시간 데이터들 sec 기준으로 변환
    playtime, advtime = play_time.split(":"), adv_time.split(":")
    playtime = int(playtime[0]) * 3600 + int(playtime[1]) * 60 + int(playtime[2])
    advtime = int(advtime[0]) * 3600 + int(advtime[1]) * 60 + int(advtime[2])

    n_count = [0] * (playtime + 1)

    for log in logs:
        lse = log.split("-")
        ls, le = lse[0].split(":"), lse[1].split(":")
        ls, le = int(ls[0]) * 3600 + int(ls[1]) * 60 + int(ls[2]), int(le[0]) * 3600 + int(le[1]) * 60 + int(le[2])

        n_count[ls] += 1
        n_count[le] -= 1

    # 특정 시간 기준 시청자 수
    for _ in range(1, len(n_count)):
        n_count[_] += n_count[_ - 1]

    # 특정 시간 기준 누적
    for _ in range(1, len(n_count)):
        n_count[_] += n_count[_ - 1]

    max_time = 0
    for start in range(-1, playtime - advtime):
        time = n_count[start + advtime] - n_count[max(start, 0)]

        if time > max_time:
            max_time = time
            answer = start + 1

    m, s = divmod(answer, 60)
    h, m = divmod(m, 60)
    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(s) if s < 10 else str(s)

    answer = h + ':' + m + ':' + s

    return answer