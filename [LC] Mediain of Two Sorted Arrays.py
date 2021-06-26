import heapq
def findMedianSortedArrays(nums1, nums2):
    answer = 0
    nums = nums1 + nums2
    if len(nums) == 0:
        return 0

    quotient, remainder = divmod(len(nums), 2)
    heapq.heapify(nums)

    if remainder == 0:  # 짝수
        for _ in range(quotient - 1):
            heapq.heappop(nums)
        for _ in range(2):
            answer += heapq.heappop(nums)
        return answer / 2

    else:  # 홀수
        for _ in range(quotient):
            heapq.heappop(nums)
        answer = heapq.heappop(nums)
        return answer

# heapify() -> O(N)
# heappop() -> O(logN)

print(findMedianSortedArrays([1,3],[2]))