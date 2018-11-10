#선택 정렬
def SelectionSort(data):
    for i in range(0, len(data)-1):
        j=i+1
        while(j < len(data)):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
            j = j+1
    return data

All = []                       #데이터 리스트입니다.
with open('data.txt') as f:     #데이터를 READ하는 모듈
    lines = f.read().split()    #data.txt  파일에 들어있는 데이터들을 line별로 읽어와서
    for line in lines:          #All리스트에 append 시켜줍니다.
        All.append(int(line))
print(All)                      #원래 파일상에 저장되어있는 500개의 데이터
print(SelectionSort(All))              #선택정렬을 통해 절렬된 이후의 데이터
