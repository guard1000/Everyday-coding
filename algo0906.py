import csv
date = input("언제여행가실 건가요? 예)2018.12.25 ")
print('일정에 맞는 경기를 찾아줄게요. 다음과 같아요. ')

f = open('liga.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    if line[1] == date:
        print(line)
f.close()

city = input("어떤 도시에서 숙박할 건가요?")
print('해당하는 도시의 숙소를 평점과 함께 추천해 드릴게요.')

f = open('house.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    if line[0].lower() == city.lower():
        print(line)
f.close()

visa = input("비자 발급 받으셨나요? Y/N")
if visa == 'Y':
    print("비행기 타러 갑시다!")
else:
    print("비자부터 발급받으러 가죠. 대사관 ㄱㄱ")

