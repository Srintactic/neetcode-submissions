class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        curr_max = 0
        for index in range(len(nums)):
            if nums[index] != 1:
               curr_max = 0
               continue
            if nums[index] == 1 and curr_max == 0:
                curr_max = 1
            else:
                curr_max += 1
            max_consecutive = max_consecutive if max_consecutive >= curr_max else curr_max
        return max_consecutive