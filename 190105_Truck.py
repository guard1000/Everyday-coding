def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    bt = []
    while True:
        if len(bt) > 0 and answer - bt[0] >= bridge_length:
            bridge.pop(0)
            bt.pop(0)

        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            bt.append(answer)
            if len(truck_weights) == 1:
                break
            truck_weights.pop(0)
        answer += 1

    answer = answer + bridge_length + 1

    return answer







bl1=2
w1=10
tw1=[7,4,5,6]
bl2=100
w2=100
tw2=[10]
bl3=100
w3=100
tw3=[10,10,10,10,10,10,10,10,10,10]

print(solution(bl1, w1, tw1))
print(solution(bl2, w2, tw2))
print(solution(bl3, w3, tw3))