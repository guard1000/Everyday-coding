def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2     #mid를 기준으로
        lefthalf = alist[:mid]  #리스트 슬라이싱으로 분할
        righthalf = alist[mid:]

        mergeSort(lefthalf)     #재귀 호출
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):     #
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist=[]

with open('data.txt') as f:     #데이터를 READ하는 모듈
    lines = f.read().split()    #data.txt  파일에 들어있는 데이터들을 line별로 읽어와서
    for line in lines:          #All리스트에 append 시켜줍니다.
        alist.append(int(line))

print('머지소팅 전')
print(alist)
mergeSort(alist)
print('머지소팅 후')
print(alist)