def solution(food_times, k):
    if sum(food_times) <= k: return -1
    if len(food_times) > k: return k+1
    n = len(food_times)
    for i in range(n):
        food_times[i] = [food_times[i],i+1]
    ft = sorted(food_times,key=lambda x:x[0])
    i,r=0,0
    while True:
        if k - (n-i)*(ft[i][0]-r) < 0:
            break
        else:
            k -= (n-i)*(ft[i][0]-r)
            r += (ft[i][0]-r)
            i += 1
    ft = sorted(ft[i:n], key = lambda x: x[1])
    return ft[k%len(ft)][1]

print(solution([3,1,2],5))
print(solution([3,1,2,5,8],13))