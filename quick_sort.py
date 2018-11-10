def quick_sorted(arr):
    if len(arr) > 1:                    #그래도 일단 원소가 2개이상은 되어야 정렬을 할 것입니다.
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
with open('data.txt') as f:     #데이터를 READ하는 모듈
    lines = f.read().split()    #data.txt  파일에 들어있는 데이터들을 line별로 읽어와서
    for line in lines:          #All리스트에 append 시켜줍니다.
        arr.append(int(line))

answer = quick_sorted(arr)
print(answer)
