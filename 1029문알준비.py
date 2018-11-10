def mySort(data):
    return int(data[0]) + int(data[1]) + int(data[2]) + int(data[3])

inp=[] # 입력
for i in range(3):
    inp.append(input().split())

rank = sorted(inp, reverse = True, key = mySort)
print(rank)

order = sorted(inp, key = lambda each: each[4])
print(order)
