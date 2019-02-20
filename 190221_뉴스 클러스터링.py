import re

def solution(str1, str2):
    # str1 = re.sub('[^A-Za-z]+', '', str1)    #정규식. A-Z나 a-z외엔 모두제거
    # str2 = re.sub('[^A-Za-z]+', '', str2)

    str1 = list(str1)  # 정규화된 결과를 한글자씩 list로 넣음
    str2 = list(str2)

    len1 = len(str1)  # 각 리스트의 길이
    len2 = len(str2)

    s1 = []  # 2문자씩 끊어 들어갈 리스트
    s2 = []

    gyo = 0  # 자카드유사도 계산을 위한 변수들
    hap = 0
    J = 0.0

    for i in range(len1 - 1):  # s1에 두글자씩 끊어 추가. 대소문자 구별X
        if 'a' <= str1[i].lower() <= 'z' and 'a' <= str1[i + 1].lower() <= 'z':
            s1.append(str1[i] + str1[i + 1])
            s1[len(s1) - 1] = s1[len(s1) - 1].lower()
    for i in range(len2 - 1):  # s2에 두글자씩 끊어 추가. 대소문자 구별X
        if 'a' <= str2[i].lower() <= 'z' and 'a' <= str2[i + 1].lower() <= 'z':
            s2.append(str2[i] + str2[i + 1])
            s2[len(s2) - 1] = s2[len(s2) - 1].lower()

    gyo = intersec(s1, s2)
    hap = union(s1, s2)
    if hap > 0:
        J = gyo / hap
        answer = int(J * 65536)
        return answer
    return 65536


def intersec(a, b):
    intersec_extend = []
    intersec_extend.extend(a)
    intersec_extend.extend(b)
    intersec_extend = list(set(intersec_extend))
    answer = []
    cnta = 0
    cntb = 0

    for m in intersec_extend:
        for n in range(len(a)):
            if a[n] == m:
                cnta += 1
        for k in range(len(b)):
            if b[k] == m:
                cntb += 1
        for o in range(min(cnta, cntb)):
            answer.append(m)
        cnta = 0
        cntb = 0
    return len(answer)


def union(a, b):
    union_extend = []
    union_extend.extend(a)
    union_extend.extend(b)
    union_extend = list(set(union_extend))
    answer = []
    cnta = 0
    cntb = 0

    for m in union_extend:
        for n in range(len(a)):
            if a[n] == m:
                cnta += 1
        for k in range(len(b)):
            if b[k] == m:
                cntb += 1
        for o in range(max(cnta, cntb)):
            answer.append(m)
        cnta = 0
        cntb = 0
    return len(answer)