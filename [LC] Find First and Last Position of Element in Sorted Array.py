class Solution:
    def searchRange(nums, target):
        # sol1 이게 통과가 되네
        if len(nums) == 0 or target not in nums:
            return [-1,-1]

        s, e = 0, len(nums)-1
        while s < e:
            if nums[s] != target:
                s += 1
            if nums[e] != target:
                e -= 1
            if nums[s] == target and nums[e] == target:
                break
        return [s,e]
        """

        # sol2 - filter
        if len(nums) == 0 or target not in nums:
            return [-1, -1]

        answer = list(filter(lambda x: nums[x] == target, range(len(nums))))
        return [answer[0], answer[-1]]
        """
