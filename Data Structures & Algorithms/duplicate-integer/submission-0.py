class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict: dict[num] = num
            else : return True
        return False
         