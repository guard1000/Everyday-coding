import heapq
def firstMissingPositive(nums):
    nums = list(set(nums))
    heapq.heapify(nums)
    while len(nums) != 0 and nums[0] <= 0:
        heapq.heappop(nums)

    answer = 1
    while len(nums) != 0 and answer == nums[0]:
        heapq.heappop(nums)
        answer += 1
    return answer

print(firstMissingPositive([1,2,0]))