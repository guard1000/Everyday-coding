#n t m 입력받기
n, t, m = map(int, input().split())
answer = ""

#timetable 입력받기
table = input().split()     #먼저 시간 통째로 입력받음
timetable = []              #타임테이블 리스트를 만들자
tn = len(table)

for i in range(tn):         #테이블의 각 원소들을 : 를 기준으로 나누어 타임테이블에 어펜드
    timetable.append(table[i].split(':'))
#이로써 timetalbe리스트 각 원소의 0번은 시 1번이 분으로 입력 완료

timetable.sort();           #타임테이블을 시간순으로 정렬

if n == 1:                  #만일 셔틀이 한대만 운영될 경우
    if m > len(timetable) and (int(timetable[m-1][0]) >= 9 and int(timetable[m-1][1]) >0): #m이 더 크거나 9시 이후에만 있을때
        answer = "09:00"
    else:
        if timetable[m-1][1] == '00':       #00분일경우, 시 를 하나 땡기고 분은 59분으로
            answer = str(int(timetable[m-1][0])-1).zfill(2) + ':' + '59'

        else: #그 외엔 분을 1개 땡김
            answer = timetable[m-1][0] + ':' + str(int(timetable[m-1][1])-1).zfill(2)

else:
    table.sort()
    table.reverse()             # table에 있는 애들을 문자열간 대소비교가 되네??? 진즉 그냥 이걸로할껄 ㅎㅎ
                                # reverse한건 pop 으로 젤 앞에서부터 셔틀타는 녀석들 보내기 위해서임
    for i in range(n):
        add = i * t             #총 몇시간 몇분 후까지 셔틀이 있는지 계산
        hour = add // 60
        minute = add % 60

        flag = str(int('09') + hour).zfill(2) + ':' + str(int('00') + minute).zfill(2) #각 셔틀이 떠난느 시간을 flag에 저장

        for j in range(m): #마지막 버스의 마지막 탑승자로 탈 수있는 타이밍을 구하자
            l = len(table)
            if i == (n - 1) and j == (m - 1):
                if table[l - 1] > flag:
                    answer = flag
                else:
                    ans = table[l - 1].split(':')
                    if ans[1] == '00':
                        answer = str(int(ans[0]) - 1).zfill(2) + ':' + '59'
                    else:
                        answer = ans[0] + ':' + str(int(ans[1]) - 1).zfill(2)

            else:
                if table[l - 1] < flag:
                    table.pop()


print(answer)
