from datetime import datetime
import copy

def InsertionSort(data):
    for i in range(1, len(data)):
        current_val = data[i]
        position = i
        while position > 0 and data[position - 1] > current_val:
            data[position] = data[position-1]
            position = position-1
        if position != i:
            data[position] = current_val
    return data

def SelectionSort(data):
    for i in range(0, len(data)-1):
        j=i+1
        while(j < len(data)):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
            j = j+1
    return data

def bubble_sort(data):
    for i in range(len(data)-1): #각 실행 한번 될 때 마다 가장 큰 녀석을 찾음.
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
    return data

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2       #중간지점 기준으로
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    answer = []  # 결과를 저장

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:  # left가 right보다 크면 right을 결과에 삽입
            answer.append(right[0])
            right.pop(0)
        else:  # left보다 right이 크면 left를 결과에 삽입
            answer.append(left[0])
            left.pop(0)

    #둘중 하나는 다 없어졌을때
    if len(left) > 0:
        answer += left
    if len(right) > 0:
        answer += right
    return answer

def quick_sorted(arr):
    if len(arr) > 1:                    #그래도 일단 원소가 2개이상은 되어야 정렬을 하겠지?
        pivot = arr[len(arr) - 1]       #피봇을 잡음.
        left, mid, right = [], [], []   #피봇보다 작은 녀석은 left, 큰건 right, 피봇과 같은 값이면 mid에
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        return quick_sorted(left) + mid + quick_sorted(right)   #left, right 녀석들은 재귀로 다시 정렬!
    else:
        return arr

arr = []
start=datetime.now()
with open('data.txt') as f:     #데이터를 READ하는 모듈
    lines = f.read().split()    #data.txt  파일에 들어있는 데이터들을 line별로 읽어와서
    for line in lines:          #All리스트에 append 시켜줍니다.
        arr.append(int(line))

#리스트들 준비!
InsertionSort_list = copy.copy(arr)
SelectionSort_list = copy.copy(arr)
BubbleSort_list = copy.copy(arr)
MergeSort_list = copy.copy(arr)
QuickSort_list = copy.copy(arr)

start=datetime.now()
print('Insertion Sort\n',InsertionSort(InsertionSort_list))
print('Insertion Sort는', datetime.now()-start, '소요 되었습니다.\n')

start=datetime.now()
print('Selection Sort\n',SelectionSort(SelectionSort_list))
print('Selection Sort는', datetime.now()-start, '소요 되었습니다.\n')

start=datetime.now()
print('Bubble Sort\n',bubble_sort(BubbleSort_list))
print('Bubble Sort는', datetime.now()-start, '소요 되었습니다.\n')

start=datetime.now()
print('Merge Sort\n',merge_sort(MergeSort_list))
print('Merge Sort는', datetime.now()-start, '소요 되었습니다.\n')

start=datetime.now()
print('Quick Sort\n',quick_sorted(QuickSort_list))
print('Quick Sort는', datetime.now()-start, '소요 되었습니다.')
