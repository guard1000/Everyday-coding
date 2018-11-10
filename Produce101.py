#2014313508 박천욱
import csv

inp = []
cnt = 0
f = open('data.csv', 'r')   #파일열어서 inp 리스트로 받음
rdr = csv.reader(f)
for line in rdr:
    inp.append(line)
    for j in range(1,6):
        inp[cnt-1][j] = int(inp[cnt-1][j])
cnt += 1
f.close()

for i in range(8): #8라운드 진행
    print(i+1, end = '')
    upgrade = int(input("주차에는어떤 능력치를 올려볼까요?\n1. 댄스  2. 보컬  3. 비주얼  4. 정치력  5.랩"))
    if upgrade < 1 or upgrade > 5:
        print("잘못입력했어요. 다시 입력하세요!")
        while (upgrade <1 or upgrade >5 ):
            print(i + 1, end='')
            upgrade = int(input("주차에는어떤 능력치를 올려볼까요?\n1. 댄스  2. 보컬  3. 비주얼  4. 정치력  5.랩"))
    if upgrade == 1:
        for r in range(101):
            if inp[r][1] < 10:
                inp[r][1] += 1
    elif upgrade == 2:
        for r in range(101):
            if inp[r][2] < 10:
                inp[r][2] += 1
    elif upgrade == 3:
        for r in range(101):
            if inp[r][3] < 10:
                inp[r][3] += 1
    elif upgrade == 4:
        for r in range(101):
            if inp[r][4] < 10:
                inp[r][4] += 1
    elif upgrade == 5:
        for r in range(101):
            if inp[r][5] < 10:
                inp[r][5] += 1

    result = sorted(inp, reverse = True, key=lambda x:(x[1]*x[2]*x[3]*x[4]*x[5]))
    num = 0
    for k in result:
        if num < 11:
            print(k[0], end = ' ')
            num += 1
    print("\n")

