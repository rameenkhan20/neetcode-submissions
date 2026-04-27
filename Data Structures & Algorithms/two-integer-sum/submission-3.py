class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in freq:
                freq[nums[i]] = i
            else:
                return [freq[val] , i]