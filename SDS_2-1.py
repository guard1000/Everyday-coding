# https://sds.elice.io/courses/640/lectures/5579/materials/3
# Python3 만 지원됩니다.
# Bin packing 문제 응용
import itertools

inp=[]  #케이스별 미사일정보 보관할 리스트
enemy=[]    #케이스별 적 정보 저장

def inpcase(n): #테스트 케이스 숫자만큼 케이스 입력
    for i in range(n):
        inp.append([])
        N, M, B = map(int, input().split()) # N M B 입력(적수, 미사일수, 방어막)
        enemy.append([N,B])
        for j in range(M):  # M번 반복 -> 마사일 정보 입력 받음
            dmg, num = map(int, input().split())
            inp[i].append([dmg,num])

def solution(enem, mis):    #적 정보와 미사일 정보를 받아옴
    answer=0
    missile=[]
    for i in range(len(mis)):   #missile변수에 미사일들 입력
        for j in range(mis[i][1]):
            missile.append(mis[i][0])

    #불가능한 경우 -1 출력
    missile = sorted(missile, reverse=True)
    if sum(missile[:3]) < enem[0]*enem[1]:  #제일 큰 4개 합이 총 방어막보다 작으면 불가
        return -1

    # 가능한 경우
    else:
        one = [n for n in missile if n >= enem[1]]  #혼자서도 격파 가능한 미사일들
        two = [m for m in missile if m < enem[1]]   #혼자서 격파 불가능한 미사일들
        c = itertools.combinations(two, 2)
        two = [list(n) for n in c if n[0] + n[1] >= enem[1]]    #합이 방어막 이상인 2개조합 리스트
        two = sorted(two, key=lambda a: sum(a))
        two = two[:enem[0]]  #enem의 갯수개 만큼만 빼냄
        two = [sum(n) for n in two] + one
        two.sort()
        for i in range(enem[0]):
            answer = answer+two[i]
        return answer





# 메인
n = int(input())    # 테스트케이스 몇개인지 입력받음
inpcase(n)
for i in range(n):
    print('#', end='')
    print(1+i,solution(enemy[i], inp[i])) #나중에 삭제
