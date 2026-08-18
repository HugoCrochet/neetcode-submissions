class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = set()
        output = []
        all = 1
        one_zero = 0
        for num in nums:
            if num in seen and num == 0: 
                return [0]*len(nums)
            else: seen.add(num)
            if num != 0: all *= num
            
        for j in range(len(nums)):
            if nums[j] == 0:
                output.append(all)
            else: 
                if 0 in seen:
                    output.append(0)
                else: output.append(int(all/nums[j]))
        return output
                    

        