def solution(food_times, k):
    answer = 0
    n = len(food_times)
    if sum(food_times) < k:
        answer = -1
    else:
        while k > 0:
            if food_times[answer] == 0 and answer < n-1:
                answer = answer +1
            elif food_times[answer] == 0 and answer == n-1:
                answer = 0
            elif food_times[answer] > 0 and  answer < n-1:
                food_times[answer] = food_times[answer]-1
                answer = answer + 1
                k = k - 1
            elif food_times[answer] > 0 and  answer == n-1:
                food_times[answer] = food_times[answer]-1
                answer = 0
                k = k - 1

    answer = answer+1
    return answer


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))