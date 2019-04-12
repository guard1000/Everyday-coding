import itertools
import copy

N = int(input())
number = list(map(int,input().split()))
sample = [i for i in range(1,N)]
oper= list(map(int, input().split()))
order = []  #1- plus, 2-minus 3-product 4-division
maximum, minimum = -1000000000,1000000000

pluscomb = itertools.combinations(sample,oper[0])
for plus in pluscomb:
    sample2 = copy.deepcopy(sample)
    sample2 = list(set(sample2) - set(plus))

    minuscomb = itertools.combinations(sample2,oper[1])
    for minus in minuscomb:
        sample3 = copy.deepcopy(sample2)
        sample3 = list(set(sample3) - set(minus))

        procomb = itertools.combinations(sample3,oper[2])
        for pro in procomb:
            sample4 = copy.deepcopy(sample3)
            sample4 = list(set(sample4) - set(pro))

            divcomb = itertools.combinations(sample4, oper[3])
            for div in divcomb:
                sample5 = copy.deepcopy(sample4)
                sample5 = list(set(sample5) - set(div))

                tmp = []
                for i in range(1,N):    #
                    if i in plus:   tmp.append(1)
                    elif i in minus:  tmp.append(2)
                    elif i in pro:  tmp.append(3)
                    elif i in div:  tmp.append(4)
                order.append(tmp)
for od in order:
    num = copy.deepcopy(number)
    for o in range(len(od)):
        if od[o] == 1:  #plus
            num[o+1] += num[o]
        elif od[o] == 2:    #minus
            num[o+1] = num[o]-num[o+1]
        elif od[o] == 3:    #mul
            num[o+1] *= num[o]
        elif od[o] == 4 and (num[o] < 0 and num[o+1] >0):    #div
            num[o+1] = -(-num[o]//num[o+1])
        elif od[o] == 4:
            num[o+1] = num[o]//num[o+1]
    if num[-1] > maximum:   maximum = num[-1]
    if num[-1] < minimum:   minimum = num[-1]

print(maximum)
print(minimum)


'''
6
1 2 3 4 5 6
2 1 1 1
'''