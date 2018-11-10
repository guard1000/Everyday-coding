#merge 연습

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

arr = [7, 1, 4, 6, 10, 2, 14, 16, 13, 11, 15, 9, 12, 5, 8, 3]
print(merge_sort(arr))



