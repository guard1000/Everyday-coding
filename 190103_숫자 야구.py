import itertools

# a와 b를 입력받았을 때 둘을 비교해 몇S 몇B인지 판단한다.
def judgement(a, b):
    strike = 0
    ball = 0
    for x in range(3):
        if a[x] == b[x]:
            strike = strike + 1
        elif a[x] in b:
            ball = ball + 1
    return [strike, ball]

def solution(baseball):
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # numlsit
    alist = []  # answer 가능한 숫자들이 저장됨. 소거법으로 진행
    answer = 0

    mypermutation = itertools.permutations(numlist, 3)  # 3자리 수 가능한 것 전체 리스트 생성
    for s in mypermutation:
        s = list(s)
        alist.append(s)

    # 이제부터 케이스들을 토대로 소거법으로 진행
    for i in range(len(baseball)):
        tmp = list(str(baseball[i][0]))  # tmp엔 부른 숫자를 쪼개어 저장
        for j in range(3):
            tmp[j] = int(tmp[j])
        cnt = 0
        while cnt < len(alist):
            if judgement(alist[cnt], tmp) != baseball[i][1:]:  # 몇 스트라잌 몇 볼인지가 같지 않다면 후보군에서 탈락
                del alist[cnt]
            else:
                cnt = cnt + 1

    answer = len(alist)
    return answer