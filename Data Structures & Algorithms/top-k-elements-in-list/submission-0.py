class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in range(len(nums)):     
            if nums[num] not in num_count:   
                num_count[nums[num]] = 1
            else:
                num_count[nums[num]] += 1
            
           
        def frequency(value):
            return num_count[value]
    
        sorted_list = sorted(num_count.keys(), key=frequency,  reverse=True)

        return sorted_list[:k]





