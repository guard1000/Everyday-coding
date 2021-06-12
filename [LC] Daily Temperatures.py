def dailyTemperatures(tempratures) :
    answer = [0] * len(tempratures)
    idx, stack = 0, []

    while idx < len(tempratures):
        while len(stack) != 0 and tempratures[stack[-1]] < tempratures[idx]:
            tar_idx = stack.pop()
            answer[tar_idx] = idx - tar_idx
        stack.append(idx)
        idx += 1

    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))

"""
    # 29개 통과하는 time limit 풀이
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        answer = [0] * len(temperatures)
        idx, counter = 1, {0:1}
        while idx < len(temperatures):
            tar_idxs = [_ for _ in counter]
            for tar_idx in tar_idxs:
                if counter[tar_idx] != 0 and temperatures[tar_idx] < temperatures[idx]: # warmer found
                    answer[tar_idx] = counter[tar_idx]
                    del(counter[tar_idx])
                else:
                    counter[tar_idx] += 1  

            counter[idx] = 1
            idx += 1

        return answer
"""