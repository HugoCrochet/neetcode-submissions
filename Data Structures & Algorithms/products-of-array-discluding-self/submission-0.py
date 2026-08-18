class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        for i in range(1,n-1):
            prefix[i] = prefix[i-1]*nums[i]
            suffix[n-i-1] = suffix[n-i]*nums[n-i-1]
        for i in range(n):
            if i>0 and i<n-1:
                res.append(prefix[i-1]*suffix[i+1])
            elif i==0:
                res.append(suffix[i+1])
            elif i ==n-1:
                res.append(prefix[i-1])
        return res
