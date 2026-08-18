class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range (0, len(nums)):
            s.add(nums[i])
        if len(s) == len(nums): return False
        return True