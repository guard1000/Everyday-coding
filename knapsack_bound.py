def get(n):
    for i in range(n):
        print(i + 1, end=' ')
        tn = input('번째 Item의 이름: ')
        items[i].append(tn)
        print(i + 1, end=' ')
        tp=int(input('번째 Item의 가치(Price): '))
        items[i].append(tp)
        print(i+1, end=' ')
        tw=int(input('번째 Item의 무게(Weight): '))
        items[i].append(tw)



def knapsack(W, items):
    n = len(items)
    k = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif items[i-1][2] <= w:
                k[i][w] = max(items[i-1][1] + k[i-1][w-items[i-1][2]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    picked = []
    set_trace(k, n, W, items, picked)
    return k[n][W], picked

def set_trace(k, n, W, items, picked):
    for i in range(n, 0, -1):
        if k[i][W] != k[i-1][W]:
            picked.append(items[i-1])
            set_trace(k, i-1, W-items[i-1][2], items, picked)
            break

items = []
n = int(input("Item 총 갯수:"))
for i in range(n):
    items.append([])
m = int(input("가방의 총가용 무게:"))
get(n)
print('\n입력: ', items)

max_value,  picked = knapsack(m, items)
print('\n 선택된 Items')
print("이름", "가치", "무게")
for item in reversed(picked):
    print(item[0], ' '*2, item[1], ' '*3, item[2])

print("\n최대 이익:", max_value)
