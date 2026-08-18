class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, reverse_suff, res = [], [], []
        pref.append(1)
        reverse_suff.append(1)
        
        for i in range(1,len(nums)):
            pref.append(pref[i-1]*nums[i-1])
            reverse_suff.append(reverse_suff[i-1]*nums[-i])
        n = len(nums)
        for j in range(n):
            res.append(pref[j]*reverse_suff[n-1-j])
        return res
        


        


                    

        