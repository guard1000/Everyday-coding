import itertools

def subsets(nums):
    answer, idxs = [[], nums], [_ for _ in range(len(nums))]

    for n in range(1, len(nums)):
        mycombination = itertools.combinations(idxs, n)  # 순열생성
        for mycomb in mycombination:
            tmp = []
            for idx in mycomb:
                tmp.append(nums[idx])
            answer.append(tmp)
    return answer

print(subsets([1,2,3]))
print(subsets([0]))