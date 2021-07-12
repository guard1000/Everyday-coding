def solution(n, stations, w):
    answer = 0
    station_idx = 0
    pos = 1
    while pos <= n:
        # station 범위 밖의 왼쪽일 때 -> 기지국 하나 설치(answer을 +1), new 기지국 범위 +1 칸으로 이동
        if station_idx == len(stations) or pos < stations[station_idx] - w:
            pos += (2 * w + 1)
            answer += 1
        # station 범위 안일 때 -> station 범위 +1 칸으로 이동, station_idx +1
        elif stations[station_idx] - w <= pos <= stations[station_idx] + w:
            pos = stations[station_idx] + w + 1
            station_idx += 1
        # station 범위 밖의 오른쪽일 때 -> station_idx만 +1
        elif stations[station_idx] + w < pos:
            station_idx += 1

    return answer