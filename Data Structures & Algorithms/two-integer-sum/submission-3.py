class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = []
        for i, num in enumerate(nums):
            nums_sorted.append([num,i])
        nums_sorted.sort()
        l, r = 0, len(nums_sorted)-1
        while l<r:
            if nums_sorted[l][0] + nums_sorted[r][0] > target:
                r -= 1 
            elif nums_sorted[l][0] + nums_sorted[r][0] < target:
                l += 1 
            else: return [min(nums_sorted[l][1],nums_sorted[r][1]),max(nums_sorted[l][1],nums_sorted[r][1])]
         
        