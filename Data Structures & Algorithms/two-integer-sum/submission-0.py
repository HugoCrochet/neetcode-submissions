class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = {}
        for index, num in enumerate(nums):
            if num in dict_sum:
                return [dict_sum[num], index]
            else: dict_sum[target-num] = index
        
