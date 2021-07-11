def solution(places):
    answer = []
    # 1. place에서 'P'(사람) 들만 추출
    for place in places:
        people = []
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    people.append([y, x])

        tmp = 1
        # 2. 각 사람별 맨해튼거리 2 이하에 위치한 'P'들 - candidates 추출
        for person in people:
            candidates = []
            for y in range(person[0] - 2, person[0] + 3):
                for x in range(person[1] - 2, person[1] + 3):
                    if (-1 < x < 5) and (-1 < y < 5) and (abs(y - person[0]) + abs(x - person[1])) <= 2 and place[y][
                        x] == 'P' and not (y == person[0] and x == person[1]):
                        candidates.append([y, x])

            y, x = person[0], person[1]  # person의 위치정보를 [y,x]로 저장

            # 3. 후보자들 대상으로 다음 조건별 거리두기 확인
            #  1) candidates 중 행 같은 경우
            #  2) candidates 중 열 같은 경우
            #  3) candidates 중 행,열 다른 경우(대각)
            for candi in candidates:
                if candi[0] == y:  # 같은 행에 있을 경우
                    if abs(x - candi[1]) == 1:  # 바로 옆인 경우 -> 거리두기 X
                        tmp = 0
                        break
                    if place[y][(x + candi[1]) // 2] == 'O':  # 두 칸 떨어져 있는경우, 가운데 'O'인지 확인
                        tmp = 0
                        break

                elif candi[1] == x:  # 같은 열에 있을 경우
                    if abs(y - candi[0]) == 1:  # 바로 위아래인 경우 -> 거리두기 X
                        tmp = 0
                        break
                    if place[(y + candi[0]) // 2][x] == 'O':  # 두 칸 떨어져 있는경우, 가운데 'O'인지 확인
                        tmp = 0
                        break
                else:  # 대각에 위치한 경우, 그 사이에 'O'가 존재하면 거리두기 X
                    y_min, x_min = min(candi[0], y), min(candi[1], x)
                    if 'O' in [place[y_min][x_min], place[y_min + 1][x_min], place[y_min][x_min + 1],
                               place[y_min + 1][x_min + 1]]:
                        tmp = 0
                        break

            if tmp == 0:  # candidates 거리두기 확인 중 1건이라도 실패시 break
                break

        answer.append(tmp)

    return answer