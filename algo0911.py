All = [] #데이터를 입력받을 리스트입니다.

with open('data.txt') as f:     #데이터를 READ하는 모듈
    lines = f.read().split()    #data.txt  파일에 들어있는 데이터들을 line별로 읽어와서
    for line in lines:          #All리스트에 append 시켜줍니다.
        All.append(line)

i = 0
num = 0
j = i
min = All[i]

while i != 500:             #i번째 인덱스에 저장된 값을 i부터 499 중 제일 작은 값으로 바꿔줍니다.
    while j != 500:         #i부터 499까지의 인덱스를 j를 이용해 탐색합니다.
        if int(All[i]) > int(All[j]):
            num = All[i]    #swap 기능입니다.
            All[i] = All[j]
            All[j] = num
            min = All[i]
        j = j+1
    i = i+1
    j = i


print(All)  #마지막 출력부분입니다.


